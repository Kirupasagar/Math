from django.shortcuts import render
def home(request):
    return render(request,'index.html')
def Power(request):
    if request.method == 'POST':
        intensity_value = int(request.POST.get('intensity-input'))
        resistance_value = int(request.POST.get('resistance-input'))
        power = (intensity_value**2)*(resistance_value)
        return render(request,'Result.html',{'output':power})
