from django.http import HttpResponse
from .dnac_manager import DNAC_Manager
from .mongo import log_action

dnac = DNAC_Manager()

def auth_view(request):
    success = dnac.get_auth_token(display_token=True)
    log_action("auth", status="success" if success else "fail")
    return HttpResponse("Authentication Done")

def devices_view(request):
    devices = dnac.get_network_devices()
    log_action("get_devices")
    
    output = "<br>".join([d['hostname'] for d in devices])
    return HttpResponse(output)

def interfaces_view(request):
    ip = request.GET.get('ip')
    interfaces = dnac.get_device_interfaces(ip)
    log_action("get_interfaces", ip=ip)

    output = "<br>".join([i['portName'] for i in interfaces])
    return HttpResponse(output)