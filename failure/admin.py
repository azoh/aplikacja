# -*- coding: utf-8 -*-
from django.contrib import admin
from datetime import datetime, date
from django.utils import timezone
from failure.models import Hala, Wydzial, Maszyna, Status, Awaria
import xlwt
from django.http import HttpResponse

def export_xls(modeladmin, request, queryset):
		response = HttpResponse(content_type='application/ms-excel')
		response['Content-Disposition'] = 'attachment; filename=hala.xls'
		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet("Hala")
		
		row_num = 0
		
		columns = [
			(u"ID", 2000),
			(u"Symbol", 6000),
			(u"User", 8000),
		]

		font_style = xlwt.XFStyle()
		font_style.font.bold = True

		for col_num in range(len(columns)):
			ws.write(row_num, col_num, columns[col_num][0], font_style)
			# set column width
			ws.col(col_num).width = columns[col_num][1]

		font_style = xlwt.XFStyle()
		font_style.alignment.wrap = 1
		
		for obj in queryset:
			row_num += 1
			row = [
				obj.pk,
				obj.symbol,
				obj.user.username,
			]
			for col_num in range(len(row)):
				ws.write(row_num, col_num, row[col_num], font_style)
				
		wb.save(response)
		return response
    
export_xls.short_description = u"Exportuj do .xls"

class HalaAdmin(admin.ModelAdmin):
	list_display = ["symbol","user"]
	list_filter = ["user"]
	list_display_links = ["symbol"]
	ordering = ["id"]
	actions = [export_xls]

def export_xls(modeladmin, request, queryset):
		response = HttpResponse(content_type='application/ms-excel')
		response['Content-Disposition'] = 'attachment; filename=wydzial.xls'
		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet("Wydzial")
		
		row_num = 0
		
		columns = [
			(u"ID", 2000),
			(u"Nazwa", 6000),
			(u"User", 8000),
		]

		font_style = xlwt.XFStyle()
		font_style.font.bold = True

		for col_num in range(len(columns)):
			ws.write(row_num, col_num, columns[col_num][0], font_style)
			# set column width
			ws.col(col_num).width = columns[col_num][1]

		font_style = xlwt.XFStyle()
		font_style.alignment.wrap = 1
		
		for obj in queryset:
			row_num += 1
			row = [
				obj.pk,
				obj.nazwa,
				obj.user.username,
			]
			for col_num in range(len(row)):
				ws.write(row_num, col_num, row[col_num], font_style)
				
		wb.save(response)
		return response
    
export_xls.short_description = u"Exportuj do .xls"

class WydzialAdmin(admin.ModelAdmin):
	list_display = ["nazwa","user"]
	list_filter = ["user"]
	list_display_links = ["nazwa"]
	ordering = ["nazwa"]
	search_fields = ["nazwa"]
	actions = [export_xls]

def export_xls(modeladmin, request, queryset):
		response = HttpResponse(content_type='application/ms-excel')
		response['Content-Disposition'] = 'attachment; filename=maszyna.xls'
		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet("Maszyna")
		
		row_num = 0
		
		columns = [
			(u"ID", 2000),
			(u"Nazwa", 6000),
			(u"Wydział", 6000),
			(u"Hala", 6000),
			(u"Opiekun", 6000),
		]

		font_style = xlwt.XFStyle()
		font_style.font.bold = True

		for col_num in range(len(columns)):
			ws.write(row_num, col_num, columns[col_num][0], font_style)
			# set column width
			ws.col(col_num).width = columns[col_num][1]

		font_style = xlwt.XFStyle()
		font_style.alignment.wrap = 1
		
		for obj in queryset:
			row_num += 1
			row = [
				obj.pk,
				obj.nazwa,
				obj.wydzial.nazwa,
				obj.hala.symbol,
				obj.opiekun.username,
			]
			for col_num in range(len(row)):
				ws.write(row_num, col_num, row[col_num], font_style)
				
		wb.save(response)
		return response
    
export_xls.short_description = u"Exportuj do .xls"

class MaszynaAdmin(admin.ModelAdmin):
	list_display = ["nazwa", "wydzial", "hala", "opiekun"]
	list_filter = ["wydzial", "hala", "opiekun"]
	list_display_links = ["nazwa"]
	search_fields = ["nazwa"]
	ordering = ["hala"]
	actions = [export_xls]

def export_xls(modeladmin, request, queryset):
		response = HttpResponse(content_type='application/ms-excel')
		response['Content-Disposition'] = 'attachment; filename=status.xls'
		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet("Status")
		
		row_num = 0
		
		columns = [
			(u"ID", 2000),
			(u"Nazwa", 6000),
		]

		font_style = xlwt.XFStyle()
		font_style.font.bold = True

		for col_num in range(len(columns)):
			ws.write(row_num, col_num, columns[col_num][0], font_style)
			# set column width
			ws.col(col_num).width = columns[col_num][1]

		font_style = xlwt.XFStyle()
		font_style.alignment.wrap = 1
		
		for obj in queryset:
			row_num += 1
			row = [
				obj.pk,
				obj.nazwa,
			]
			for col_num in range(len(row)):
				ws.write(row_num, col_num, row[col_num], font_style)
				
		wb.save(response)
		return response
    
export_xls.short_description = u"Exportuj do .xls"

class StatusAdmin(admin.ModelAdmin):
	list_display = ["nazwa"]
	list_display_links = ["nazwa"]
	ordering = ["id"]
	actions = [export_xls]

def export_xls(modeladmin, request, queryset):
		response = HttpResponse(content_type='application/ms-excel')
		response['Content-Disposition'] = 'attachment; filename=awaria.xls'
		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet("Awaria")
		
		row_num = 0
		
		columns = [
			(u"ID", 2000),
			(u"Maszyna", 6000),
			(u"Wydział", 6000),
			(u"Opis awarii", 6000),
			(u"Zgłaszający", 6000),
			(u"Status", 6000),
		]

		font_style = xlwt.XFStyle()
		font_style.font.bold = True

		for col_num in range(len(columns)):
			ws.write(row_num, col_num, columns[col_num][0], font_style)
			# set column width
			ws.col(col_num).width = columns[col_num][1]

		font_style = xlwt.XFStyle()
		font_style.alignment.wrap = 1
		
		for obj in queryset:
			row_num += 1
			row = [
				obj.pk,
				obj.maszyna.nazwa,
				obj.wydzial.nazwa,
				obj.description,
				obj.user.username,
				obj.status.nazwa,
			]
			for col_num in range(len(row)):
				ws.write(row_num, col_num, row[col_num], font_style)
				
		wb.save(response)
		return response
    
export_xls.short_description = u"Exportuj do .xls"

class AwariaAdmin(admin.ModelAdmin):
	list_display = ["maszyna", "wydzial", "description", "add_date", "user", "sur", "repair_date", "remove_date", "status"]
	exclude = ["user","add_date"]
	list_filter = ["wydzial", "add_date", "status"]
	list_display_links = ["status", "description"]
	search_fields = ["maszyna", "sur"]
	ordering = ("status", "add_date")
	actions = [export_xls]

	def save_model(self, request, obj, form, change):
         obj.user = request.user
         obj.save()

admin.site.register(Hala, HalaAdmin)
admin.site.register(Wydzial, WydzialAdmin)
admin.site.register(Maszyna, MaszynaAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Awaria, AwariaAdmin)