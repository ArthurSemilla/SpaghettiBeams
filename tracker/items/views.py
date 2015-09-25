from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def generate_item(request):
	"""
		name: "name"
		owned: true/false
		tracked: true/false
	"""
	data = json.loads(request.body.decode('utf-8'))

	item = Item(name = data['name'])

	if 'owned' in data:
		item.owned = data['owned']

	if 'tracked' in data:
		item.tracked = data['tracked']

	item.save()

	if homework.id
		return JsonResponse({"success": True})
	else
		return JsonResponse({"success": False})