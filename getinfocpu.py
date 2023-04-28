import cpuinfo
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def form(path):
    my_canvas = canvas.Canvas(path, pagesize=letter)
    my_canvas.setLineWidth(.3)
    my_canvas.setFont('Helvetica', 20)
    my_canvas.drawString(200, 750, 'Compito Mendolia Valerio')
    my_canvas.setFont('Helvetica', 12)
    my_canvas.drawString(30, 700, 'Utilizzo di Python per generare le caratteristiche della mia CPU salvando le informazioni in un file PDF')
    my_canvas.drawString(30, 670,'Informazioni Generali: ' + cpuinfo.get_cpu_info()['brand_raw'])
    my_canvas.drawString(30, 650, 'Architettura di sistema: ' + cpuinfo.get_cpu_info()['arch_string_raw'])
    my_canvas.drawString(30, 630, 'Versione CPU: ' + cpuinfo.get_cpu_info()['cpuinfo_version_string'])
    my_canvas.drawString(30, 610, 'Velocità processore: ' + cpuinfo.get_cpu_info()['hz_advertised_friendly'])
    my_canvas.drawString(30, 590, 'Utilizzo della velocità del processore in questo momento: ' + cpuinfo.get_cpu_info()['hz_actual_friendly'])
    my_canvas.drawString(30, 570, 'Multi-Core: ' + str(cpuinfo.get_cpu_info()['count']))
    my_canvas.drawString(30, 550, 'Bits: ' + str(cpuinfo.get_cpu_info()['bits']))
    my_canvas.drawString(30, 530, 'Modello numerico: ' + str(cpuinfo.get_cpu_info()['model']))
    my_canvas.drawString(30, 510, 'Famiglia del processore in numeri: ' + str(cpuinfo.get_cpu_info()['family']))
    my_canvas.drawString(30, 490, 'Venditore: ' + cpuinfo.get_cpu_info()['vendor_id_raw'])
    my_canvas.drawString(30, 470, 'Dimensione delle cache L2: ' + str(cpuinfo.get_cpu_info()['l2_cache_size']))
    my_canvas.drawString(30, 450, 'Dimensione delle cache L3: ' + str(cpuinfo.get_cpu_info()['l3_cache_size']))
    my_canvas.save()
if __name__ == '__main__':
    form('cpucompilato.pdf')

print("Documento salvato con successo")

#print('CPU =', cpuinfo.get_cpu_info()['brand_raw'])