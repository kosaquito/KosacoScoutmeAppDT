from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, ListFlowable, ListItem, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os

def create_user_manual():
    print("Generando Manual de Usuario...")
    doc = SimpleDocTemplate("Manual_Usuario.pdf", pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=72)
    
    styles = getSampleStyleSheet()
    
    # Estilos Personalizados
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
        fontSize=18,
        spaceBefore=20,
        spaceAfter=15,
        textColor=colors.HexColor('#283593'),
        keepWithNext=True
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=14,
        spaceBefore=15,
        spaceAfter=10,
        textColor=colors.HexColor('#303f9f'),
        keepWithNext=True
    )
    
    body_style = styles['Normal']
    body_style.fontSize = 11
    body_style.leading = 14
    body_style.spaceAfter = 10
    
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=body_style,
        leftIndent=20
    )

    story = []

    # --- PORTADA ---
    # Logo
    logo_path = os.path.join('assets', 'Pelota.png')
    if os.path.exists(logo_path):
        img = Image(logo_path, width=2*inch, height=2*inch)
        story.append(Spacer(1, 100))
        story.append(img)
        story.append(Spacer(1, 12))

    story.append(Paragraph("Manual de Usuario", title_style))
    story.append(Paragraph("Kosaco ScoutMe v1.0", styles['Title']))
    story.append(Spacer(1, 100))
    story.append(Paragraph("Sistema de Gestión Integral para Futbolistas", styles['Heading2']))
    story.append(PageBreak())

    # --- INTRODUCCIÓN ---
    story.append(Paragraph("1. Introducción", heading_style))
    story.append(Paragraph("Bienvenido a <b>Kosaco ScoutMe</b>. Este sistema ha sido diseñado para profesionalizar la gestión de su carrera futbolística. En el fútbol moderno, los datos son tan importantes como el talento. Este manual le guiará paso a paso para sacar el máximo provecho de su herramienta.", body_style))
    
    story.append(Paragraph("Importancia de los Datos Actualizados", subheading_style))
    story.append(Paragraph("Mantener su información al día es crucial por tres razones:", body_style))
    story.append(ListFlowable([
        ListItem(Paragraph("<b>Visibilidad:</b> Los scouts buscan datos recientes. Un perfil desactualizado es una oportunidad perdida.", bullet_style)),
        ListItem(Paragraph("<b>Análisis Real:</b> Solo con datos actuales podrá ver su evolución real y corregir deficiencias a tiempo.", bullet_style)),
        ListItem(Paragraph("<b>Imagen Profesional:</b> Un CV con datos de hace 6 meses transmite dejadez. Uno actualizado transmite compromiso y profesionalismo.", bullet_style))
    ], bulletType='bullet', start='circle'))

    # --- INSTALACIÓN ---
    story.append(Paragraph("2. Instalación y Puesta en Marcha", heading_style))
    story.append(Paragraph("Kosaco ScoutMe es un sistema <b>Portable</b>. Esto significa:", body_style))
    story.append(ListFlowable([
        ListItem(Paragraph("No requiere instalación complicada.", bullet_style)),
        ListItem(Paragraph("Puede llevarlo en un pendrive y usarlo en cualquier PC con Windows.", bullet_style)),
        ListItem(Paragraph("<b>Importante:</b> La carpeta del programa contiene un archivo llamado <i>kosaco_scoutme.db</i>. ¡Nunca borre este archivo! Ahí se guardan todos sus datos.", bullet_style))
    ], bulletType='bullet', start='circle'))
    
    story.append(Paragraph("Pasos para iniciar:", subheading_style))
    story.append(ListFlowable([
        ListItem(Paragraph("1. Descomprima la carpeta 'Release' en su PC.", bullet_style)),
        ListItem(Paragraph("2. Haga doble clic en <b>KosacoScoutMe.exe</b>.", bullet_style)),
        ListItem(Paragraph("3. ¡Listo! El sistema se abrirá.", bullet_style))
    ], bulletType='1', start='1'))

    # --- GUIA PASO A PASO ---
    story.append(Paragraph("3. Guía Paso a Paso: Módulos del Sistema", heading_style))
    
    # Datos Personales
    story.append(Paragraph("A. Datos Personales (Perfil)", subheading_style))
    story.append(Paragraph("Es la pantalla principal. Aquí se define quién es usted.", body_style))
    story.append(ListFlowable([
        ListItem(Paragraph("<b>Foto:</b> Cargue una foto profesional con la camiseta de su equipo actual.", bullet_style)),
        ListItem(Paragraph("<b>Redes Sociales:</b> El sistema validará sus enlaces. Si tiene canal de YouTube con sus mejores jugadas, es vital ponerlo aquí para que aparezca en los reportes.", bullet_style)),
        ListItem(Paragraph("<b>Datos de Contacto:</b> Mantenga su teléfono y email siempre actualizados para que los clubes puedan contactarlo.", bullet_style))
    ], bulletType='bullet', start='circle'))

    # Características
    story.append(Paragraph("B. Características Físicas", subheading_style))
    story.append(Paragraph("Registre periódicamente su peso y estatura. El sistema guardará un historial para que pueda ver su evolución gráfica a lo largo del tiempo.", body_style))

    # Trayectoria
    story.append(Paragraph("C. Trayectoria Deportiva", subheading_style))
    story.append(Paragraph("Su currículum deportivo. Agregue cada club donde ha jugado.", body_style))
    story.append(Paragraph("<b>Consejo:</b> Sea detallado en la sección de 'Logros'. Mencione campeonatos, ascensos o capitanías.", body_style))

    # Habilidades
    story.append(Paragraph("D. Habilidades y Deficiencias (Radar)", subheading_style))
    story.append(Paragraph("Aquí califica sus atributos técnicos, tácticos y físicos del 1 al 100.", body_style))
    story.append(Paragraph("Estos datos generan el <b>Gráfico de Radar</b> que es lo primero que miran los analistas. Sea honesto pero destaque sus fortalezas.", body_style))

    # Tests Físicos
    story.append(Paragraph("E. Tests Físicos", subheading_style))
    story.append(Paragraph("Registre resultados de pruebas estándar (Velocidad, Resistencia, etc.). Si tiene un preparador físico, pídale estos datos. Son evidencia objetiva de su condición atlética.", body_style))

    # Estadísticas
    story.append(Paragraph("F. Estadísticas de Juego", subheading_style))
    story.append(Paragraph("Después de cada partido, cargue sus minutos, goles, y tarjetas. Esto construirá un promedio de rendimiento que hablará por sí solo.", body_style))

    # --- REPORTES ---
    story.append(Paragraph("4. Generación de Reportes", heading_style))
    story.append(Paragraph("Esta es la función estrella de Kosaco ScoutMe.", body_style))
    story.append(Paragraph("Vaya a la pestaña 'Reportes'. Con un solo clic podrá generar:", body_style))
    story.append(ListFlowable([
        ListItem(Paragraph("<b>CV Deportivo (PDF):</b> Un documento profesional listo para enviar por WhatsApp o Email a representantes.", bullet_style)),
        ListItem(Paragraph("<b>Reporte Gráfico:</b> Ideal para compartir en redes sociales.", bullet_style))
    ], bulletType='bullet', start='circle'))

    # --- VENTAJAS ---
    story.append(Paragraph("5. Ventajas de Usar Kosaco ScoutMe", heading_style))
    story.append(ListFlowable([
        ListItem(Paragraph("<b>Centralización:</b> Deje de tener datos dispersos en notas del celular o excel.", bullet_style)),
        ListItem(Paragraph("<b>Profesionalismo:</b> Diferénciese del resto presentando informes de calidad.", bullet_style)),
        ListItem(Paragraph("<b>Autonomía:</b> No dependa de terceros para armar su CV.", bullet_style))
    ], bulletType='bullet', start='circle'))

    story.append(Spacer(1, 30))
    story.append(Paragraph("Gracias por confiar en Kosaco ScoutMe.", styles['Italic']))

    doc.build(story)
    print("Manual generado exitosamente: Manual_Usuario.pdf")

if __name__ == "__main__":
    create_user_manual()
