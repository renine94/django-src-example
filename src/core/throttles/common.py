from datetime import timedelta

from django.utils import timezone
from rest_framework.throttling import BaseThrottle


class DailyThrottle(BaseThrottle):
    """하루동안 10번 요청 허용 (자정되면 초기화)"""

    def __init__(self):
        self.request_count = 0
        self.reset_time = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)

    def allow_request(self, request, view) -> bool:
        now = timezone.now()

        if now >= self.reset_time + timedelta(days=1):
            # Reset count and reset time if it's a new day
            self.request_count = 0
            self.reset_time = now.replace(hour=0, minute=0, second=0, microsecond=0)

        if self.request_count >= 10:
            # Allow only 10 requests per day
            return False

        self.request_count += 1
        return True

    def wait(self) -> int | None:
        timezone.get_current_timezone()
        timezone.now().astimezone(timezone.get_current_timezone()).replace(hour=0, minute=0, second=0, microsecond=0)

        current_time = timezone.now()
        next_midnight = current_time.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        return (next_midnight - current_time).seconds
