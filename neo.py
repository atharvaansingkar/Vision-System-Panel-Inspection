import neoapi
result = 0
try:
    camera = neoapi.Cam()
    camera.Connect()
    
    if camera.IsConnected():
        print(camera.f.ExposureTime.value)
    
    for i in range(1, 3):  
        image = camera.GetImage()
        filename = f"captured_image.bmp"  
        image.Save(filename)
        
except (neoapi.NeoException, Exception) as exc:
    print('error: camera is not connected', exc)
    result = 1