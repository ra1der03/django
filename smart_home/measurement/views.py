# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.serializers import MeasurementSerializer, SensorSerializer, SensorDetailSerializer
from measurement.models import Measurement, Sensor


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class MeasurementModView(RetrieveAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def patch(self, request, pk):
        if request.data.get('sensor'):
            Measurement.objects.filter(id=pk).update(sensor_id=request.data.get('sensor'))
        if request.data.get('temperature'):
            Measurement.objects.filter(id=pk).update(temperature=request.data.get('temperature'))
        return Response({'res': Response.status_code})


class SensorAddView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        Sensor.objects.create(name=request.data.get('name'), description=request.data.get('description'))
        return Response({'status': Response.status_code})


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorModView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
