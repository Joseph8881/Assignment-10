from django.http import HttpResponse
from .dnac_manager import DNAC_Manager
from .mongo import log_action

dnac = DNAC_Manager()

def auth_view(request):
    success = dnac.get_auth_token()
    
    if success:
        token = dnac.token
        log_action("auth", status="success")
        return HttpResponse(f"<h2>Authentication Token:</h2><p>{token}</p>")
    else:
        log_action("auth", status="fail")
        return HttpResponse("Authentication Failed")

def devices_view(request):
    devices = dnac.get_network_devices()
    log_action("get_devices")

    html = "<h2>Network Devices</h2><table border='1'>"
    html += "<tr><th>Hostname</th><th>IP</th><th>Platform</th><th>Status</th></tr>"

    for d in devices:
        html += f"<tr><td>{d.get('hostname')}</td><td>{d.get('managementIpAddress')}</td><td>{d.get('platformId')}</td><td>{d.get('reachabilityStatus')}</td></tr>"

    html += "</table>"
    return HttpResponse(html)

def interfaces_view(request):
    ip = request.GET.get('ip')
    interfaces = dnac.get_device_interfaces(ip)
    log_action("get_interfaces", ip=ip)

    html = f"<h2>Interfaces for {ip}</h2><table border='1'>"
    html += "<tr><th>Interface</th><th>Status</th><th>VLAN</th><th>Speed</th></tr>"

    for i in interfaces:
        html += f"<tr><td>{i.get('portName')}</td><td>{i.get('status')}</td><td>{i.get('vlanId')}</td><td>{i.get('speed')}</td></tr>"

    html += "</table>"
    return HttpResponse(html)