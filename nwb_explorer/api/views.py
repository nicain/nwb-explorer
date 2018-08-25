from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import logging
import model as pygeppetto
from ..nwb_model_interpreter import NWBModelInterpreter
from ..plots_controller import PlotsController
from model.model_serializer import GeppettoModelSerializer

geppetto_model = None

#curl -X POST http://localhost:8000/api/load
@api_view(['GET','POST'])
@permission_classes((AllowAny, ))
def load(request):
    if request.method == 'GET':

        model_interpreter = NWBModelInterpreter()
        geppetto_model = model_interpreter.importType('./test_data/mem_potential_real.nwb','','','')
        serialized_model = GeppettoModelSerializer().serialize(geppetto_model)
        return Response(serialized_model)
    elif request.method == 'POST':
        return Response("Post model")

#curl -X POST http://localhost:8000/api/plot
@api_view(['GET','POST'])
@permission_classes((AllowAny, ))
def plot(request):
    if request.method == 'GET':
        plot_controller = PlotsController(geppetto_model)
        return Response(plot_controller.plot_mean())
    elif request.method == 'POST':
        return Response("Post model")

