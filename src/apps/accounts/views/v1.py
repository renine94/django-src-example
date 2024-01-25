import asyncio
import httpx
from typing import Self, Any

from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


def index(request):
    return JsonResponse("hello accounts v1", safe=False)


class TestAPI(APIView):
    def get(self: Self, request: Request, pk: int) -> Response:
        data = asyncio.run(self.aget_data(pk))
        return Response({'message': data})

    # def get(self: Self, request: Request, pk: int) -> Response:
    #     data = []
    #     for i in range(1, pk):
    #         response = httpx.get(f'https://jsonplaceholder.typicode.com/posts/{i}')
    #         data.append(response.json())
    #     return Response({'message': data})

    @staticmethod
    async def aget_data(count: int) -> list[dict] | Any:
        async def aget(post_id: int):
            async with httpx.AsyncClient() as client:
                response = await client.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
                data = response.json()
            return data

        tasks = [aget(i) for i in range(1, count + 1)]
        result = await asyncio.gather(*tasks)
        return result
