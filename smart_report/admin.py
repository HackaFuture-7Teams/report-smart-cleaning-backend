from django.contrib.gis import admin

from smart_report.model import RawData


@admin.register(RawData)
class TransactionAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ('platform', 'sender_id', 'receive_id'   , 'ack_date')}),)
    list_display = ('platform', 'sender_id', 'receive_id', 'body_json', 'ack_date',)
    readonly_fields = ('ack_date',)
