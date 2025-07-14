from faker import Faker
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

fake = Faker()

# Configuración
NUM_CVS = 50  # Cambia a 100 si deseas generar 100 CV
OUTPUT_DIR = "cv_files"

# Crear carpeta de salida si no existe
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generar_cv_pdf(filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Datos falsos
    name = fake.name()
    address = fake.address().replace("\n", ", ")
    email = fake.email()
    phone = fake.phone_number()
    summary = fake.text(max_nb_chars=300)
    experiences = [fake.job() for _ in range(3)]
    education = [f"{fake.job()} at {fake.company()}" for _ in range(2)]

    # Escribir en el PDF
    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, name)

    y -= 30
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Email: {email} | Tel: {phone}")

    y -= 20
    c.drawString(50, y, f"Dirección: {address}")

    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Resumen:")
    y -= 20
    c.setFont("Helvetica", 12)
    for line in summary.split('. '):
        c.drawString(50, y, line.strip())
        y -= 15

    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Experiencia:")
    y -= 20
    c.setFont("Helvetica", 12)
    for exp in experiences:
        c.drawString(70, y, f"- {exp}")
        y -= 15

    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Educación:")
    y -= 20
    c.setFont("Helvetica", 12)
    for edu in education:
        c.drawString(70, y, f"- {edu}")
        y -= 15

    c.save()

# Generar múltiples CVs
for i in range(1, NUM_CVS + 1):
    filename = os.path.join(OUTPUT_DIR, f"cv_{i}.pdf")
    generar_cv_pdf(filename)
    print(f"Generado: {filename}")

print(f"\n✅ Generados {NUM_CVS} CVs de prueba en la carpeta '{OUTPUT_DIR}'")
