import requests

def get_trambus_schedule(stop_id: str):
    url = f"https://jakdojade.pl/krakow/Dworzec Główny Zachód/Wawel?fn=Dworzec Główny Zachód&tn=Wawel&tc=50.054456:19.939759&fc=50.06768:19.94523&fsn=Dworzec Główny Zachód&tsn=Wawel&ft=LOCATION_TYPE_STOP&tt=LOCATION_TYPE_STOP&d=17.02.19&h=16:35&aro=1&t=1&rc=3&ri=1&r=0"
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.headers.get('content-type', '').startswith('application/json'):
            return response.json()
        else:
            return {
                "status": "success",
                "message": "Link to jakdojade.pl",
                "url": url,
                "content_type": response.headers.get('content-type', 'unknown')
            }
    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": f"Error while fetching data: {str(e)}"
        }
    except Exception as e:
        return {
            "status": "error", 
            "message": f"Unexpecter error: {str(e)}"
        }