from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os

def create_sales_report():
    doc = SimpleDocTemplate("Informe_Ventas_Kosaco_ScoutMe.pdf", pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=72)
    
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        textColor=colors.HexColor('#1a237e'), # Dark Blue
        alignment=1 # Center
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceBefore=20,
        spaceAfter=10,
        textColor=colors.HexColor('#283593')
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=12,
        spaceBefore=10,
        spaceAfter=5,
        textColor=colors.HexColor('#303f9f')
    )
    
    body_style = styles['Normal']
    body_style.fontSize = 11
    body_style.leading = 14
    
    quote_style = ParagraphStyle(
        'Quote',
        parent=styles['Italic'],
        fontSize=12,
        leftIndent=20,
        rightIndent=20,
        spaceBefore=20,
        textColor=colors.grey
    )

    story = []

    # Logo
    logo_path = os.path.join('assets', 'Logo_Blanco.png')
    if os.path.exists(logo_path):
        # Create a background for the white logo if needed, or just place it
        # Since it's "Logo_Blanco", it might be white text on transparent. 
        # If the PDF background is white, it might be invisible.
        # Let's check if there's a colored version or assume it works on white 
        # (or maybe it's "Blanco" background?). 
        # Given the name, it's likely white. Let's try to use it, but maybe put a dark rect behind it?
        # Or maybe use Pelota.png which we know is visible.
        # Let's use Pelota.png for safety as an icon, or try Logo_Blanco.
        # Actually, let's use Pelota.png as a safe bet for the header icon.
        icon_path = os.path.join('assets', 'Pelota.png')
        if os.path.exists(icon_path):
            img = Image(icon_path, width=1*inch, height=1*inch)
            story.append(img)
            story.append(Spacer(1, 12))

    # Title
    story.append(Paragraph("Kosaco ScoutMe", title_style))
    story.append(Paragraph("Informe del Sistema y Propuesta de Valor", styles['Title']))
    story.append(Spacer(1, 12))

    # Resumen Ejecutivo
    story.append(Paragraph("Resumen Ejecutivo", heading_style))
    story.append(Paragraph("<b>Kosaco ScoutMe</b> es una solución integral de software diseñada para la gestión profesional de carreras futbolísticas. No es solo una base de datos; es una herramienta estratégica que permite a jugadores, representantes y scouts centralizar, analizar y presentar información clave para potenciar el desarrollo y la visibilidad del talento deportivo.", body_style))

    # Características Principales
    story.append(Paragraph("Características Principales del Sistema", heading_style))
    story.append(Paragraph("El sistema abarca todas las dimensiones de un atleta de alto rendimiento:", body_style))
    story.append(Spacer(1, 10))

    # Feature 1
    story.append(Paragraph("1. Gestión de Identidad Digital y Profesional", subheading_style))
    story.append(ListFlowable([
        ListItem(Paragraph("<b>Datos Personales Completos:</b> Centralización de información vital.", body_style)),
        ListItem(Paragraph("<b>Integración de Redes Sociales:</b> Conexión directa con Instagram, Facebook, X (Twitter), TikTok, YouTube y LinkedIn.", body_style)),
        ListItem(Paragraph("<b>Validación de Visibilidad:</b> Alertas inteligentes que fomentan la creación de contenido en video (YouTube).", body_style))
    ], bulletType='bullet', start='circle'))

    # Feature 2
    story.append(Paragraph("2. Análisis Deportivo Profundo", subheading_style))
    story.append(ListFlowable([
        ListItem(Paragraph("<b>Evaluación de Habilidades:</b> Gráficos de radar visuales para fortalezas y debilidades.", body_style)),
        ListItem(Paragraph("<b>Evolución Física:</b> Seguimiento histórico de estatura, peso y características antropométricas.", body_style)),
        ListItem(Paragraph("<b>Tests Físicos:</b> Registro detallado de pruebas de velocidad, resistencia, fuerza y agilidad.", body_style))
    ], bulletType='bullet', start='circle'))

    # Feature 3
    story.append(Paragraph("3. Historial y Trayectoria", subheading_style))
    story.append(ListFlowable([
        ListItem(Paragraph("<b>Registro de Carrera:</b> Historial cronológico de equipos, categorías y logros.", body_style)),
        ListItem(Paragraph("<b>Estadísticas de Juego:</b> Minutos jugados, goles, asistencias, tarjetas y resultados de partidos.", body_style))
    ], bulletType='bullet', start='circle'))

    # Feature 4
    story.append(Paragraph("4. Salud y Disciplina", subheading_style))
    story.append(ListFlowable([
        ListItem(Paragraph("<b>Controles Médicos:</b> Seguimiento de aptitud física y chequeos médicos.", body_style)),
        ListItem(Paragraph("<b>Sanciones:</b> Registro transparente de conducta y sanciones disciplinarias.", body_style))
    ], bulletType='bullet', start='circle'))

    # Feature 5
    story.append(Paragraph("5. Generación de Reportes Profesionales", subheading_style))
    story.append(ListFlowable([
        ListItem(Paragraph("<b>CV Deportivo Automático:</b> Generación instantánea de currículums en PDF listos para enviar a clubes.", body_style)),
        ListItem(Paragraph("<b>Reportes Gráficos:</b> Exportación de gráficos de rendimiento y evolución.", body_style))
    ], bulletType='bullet', start='circle'))

    # Ventajas Competitivas
    story.append(Paragraph("Ventajas Competitivas y Beneficios", heading_style))

    story.append(Paragraph("🚀 Para el Jugador: \"Tu Carrera, Tu Empresa\"", subheading_style))
    story.append(ListFlowable([
        ListItem(Paragraph("<b>Profesionalismo Inmediato:</b> Presenta un CV generado por sistema que transmite seriedad.", body_style)),
        ListItem(Paragraph("<b>Visibilidad Aumentada:</b> Integra y valida tus redes sociales para mostrarte al mundo.", body_style)),
        ListItem(Paragraph("<b>Autoconocimiento:</b> Visualiza claramente dónde estás y qué necesitas mejorar.", body_style))
    ], bulletType='bullet', start='circle'))

    story.append(Paragraph("👔 Para Representantes y Agentes: \"Gestión Eficiente\"", subheading_style))
    story.append(ListFlowable([
        ListItem(Paragraph("<b>Centralización de Cartera:</b> Toda la información de tus jugadores en un solo lugar seguro.", body_style)),
        ListItem(Paragraph("<b>Toma de Decisiones:</b> Analiza la evolución con datos históricos.", body_style)),
        ListItem(Paragraph("<b>Ahorro de Tiempo:</b> Genera reportes completos en segundos.", body_style))
    ], bulletType='bullet', start='circle'))

    story.append(Paragraph("🔍 Para Scouts y Clubes: \"Información Confiable\"", subheading_style))
    story.append(ListFlowable([
        ListItem(Paragraph("<b>Estandarización:</b> Recibe información estructurada y comparable.", body_style)),
        ListItem(Paragraph("<b>Visión 360°:</b> Perfiles psicológicos, médicos y físicos en un solo reporte.", body_style))
    ], bulletType='bullet', start='circle'))

    # Conclusión
    story.append(Paragraph("Conclusión", heading_style))
    story.append(Paragraph("<b>Kosaco ScoutMe</b> transforma la manera en que se gestiona el talento futbolístico. Pasa de la informalidad a la gestión profesional de datos. En un mercado tan competitivo, tener la información organizada, accesible y bien presentada no es un lujo, es una ventaja competitiva esencial.", body_style))
    
    story.append(Paragraph('"El talento te lleva al campo, pero la gestión profesional construye una carrera."', quote_style))

    doc.build(story)
    print("PDF generado exitosamente: Informe_Ventas_Kosaco_ScoutMe.pdf")

if __name__ == "__main__":
    create_sales_report()
