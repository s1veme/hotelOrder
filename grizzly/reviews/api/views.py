from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework.views import APIView

from .serializers import ReviewSerialazer

from ..models import Review


class ReviewView(APIView):

    def get(self, request):
        # TODO: удалить данную функцию

        queryset = Review.objects.all()
        serializer = ReviewSerialazer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):
        review = request.data
        print(review)

        serializer = ReviewSerialazer(data=review)
        if serializer.is_valid(raise_exception=True):
            review_saved = serializer.save()

        return Response({'success': f'Review {review_saved.email} created successfully'})

    @classmethod
    def get_extra_actions(cls):
        return []
