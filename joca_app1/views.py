from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def primer(request):
    html="<title>View1</title> <h1> Este es el primer view de la primera Aplicacion</h1><br><p>Desde aqui se puede acceder a Google c:</p><a href='http://google.com' class='button'>Ir a Google</a>"
    return HttpResponse(html)

def HorayFecha(request):
	date = datetime.datetime.now()
	s= "<title>Fecha y Hora</title><h1>La <u>hora y fecha</u> actual en <h1><br><iframe src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAARMAAAC3CAMAAAAGjUrGAAAAjVBMVEXXKx////8AOabVGADsq6kAMKPcKhR6icQAOaqLMnBvgcEAN6UAIKAAJqEAK6IANaUAHJ8cRqsAIqAAKqPw8/mElcslTK3h5vKcqdQ1VrDO1ep8kMnW3O3Hz+YAL6TByuRnfMC7w+Fedr0AE54+XLKotNmRodBPabjo7PayvN0JPqiNnM0XRKpXcLusYYMErVt0AAACvUlEQVR4nO3Z21LiQBCAYchull0myYRwFBFQATnovv/jLUFAoRNmtJYLOv93p9JW5S97CLEWXE3YqN+mGk0Emkg0kWgi0USiiUQTiSYSTSSaSDSRaCLRRKKJRBOJJhJNJJpINJFoItFE+loTa2hyfpX3rS9EqUaTbHQ/pskJY+vDjCbiItv+y1OJJtlDvd4IafKJybavn8Q0+XyNzXxg7L08VWgST/KBpvfyVKCJSXYD/stTgSbh9H0i9l2eCjSJH98nnnyXR38TE+8nHn2XR3+T8OkwEnkuj/4mh9XxXx59TWx46vk4skrPfmQr0sROG80Tm+NIZ3r6k8asOIq+Jr2+76+Yh8UHjLomgU0XXr+g85KVnLn6mmxP1VnHPf8Qlp64GpsEYTJxjXfT8jdmlU0Ck16+rGWvfSmpyiZBkFw6aldZybuw7ibbo3ZeNjp13NCqbRKY6K1wcLR2PcLX2yQIxmYo5wbRxb3R3iSwz+L9Zxq5x1Q3CaLl+dggqXgTeyfGlmnFmyQDOddzHie6m0QF9ygey6O5ie0VzPXdy6O5SfLxAXn48anQvTyam6TH1Vmk4fFWZeFcHsVNjqvTmcXbT4Xd/Vd95x2K4ibJ/qnjpL17UtK+29+stFzLo7hJNNq9sHF4UmLj1e4bG9fy6G1iX/OX9VsfBUy0+y/pyLU8epuM89WZn37iS17zv521439fepvkq/N2/hjapttb267jYYHaJsbUh7bg4uOXjmt51DYZbxbFj6HDcNir6HM2sy57ezGJ40BR2yS4cN2VPWO/jyY0oQlNaEITgSYSTSSaSDSRaCLRRKKJRBOJJhJNJJpINJFoItFEoolEE4kmEk2k2u+rGd9skz/X8/fnbar9uqIft6kGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwn/wDJO2jfQRdhfEAAAAASUVORK5CYII=' frameborder='0'></iframe> <i><br>" + str(date) + "</i> <br>"

	return HttpResponse(s)




