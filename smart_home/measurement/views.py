# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.serializers import MeasurementSerializer, SensorSerializer
from measurement.models import Measurement, Sensor


class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        Measurement.objects.create(sensor_id=Sensor.objects.filter(id=request.data.get('sensor'))[0],
                                   temperature=request.data.get('temperature'))
        return Response({'status': Response.status_code})


class MeasurementModView(RetrieveAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def patch(self, request, pk):
        if request.data.get('sensor'):
            Measurement.objects.filter(id=pk).update(sensor_id=request.data.get('sensor'))
        if request.data.get('temperature'):
            Measurement.objects.filter(id=pk).update(temperature=request.data.get('temperature'))
        return Response({'res': Response.status_code})


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        Sensor.objects.create(name=request.data.get('name'), description=request.data.get('description'))
        return Response({'status': Response.status_code})


class SensorModView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def patch(self, request, pk):
        if request.data.get('name'):
            Sensor.objects.filter(id=pk).update(name=request.data.get('name'))
        if request.data.get('description'):
            Sensor.objects.filter(id=pk).update(description=request.data.get('description'))
        return Response({'res': Response.status_code})

