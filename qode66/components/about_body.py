import reflex as rx
import qode66.styles.styles as styles

from qode66.styles.colors import Color as Color

def about_body() -> rx.Component:
    return rx.container(

# Secció 1. Quant a
        
        rx.section(
            rx.heading(
                "Quant a",
                color=Color.ACCENT1.value,
                font_size="40px",
                margin_bottom="20px",
            ),
            rx.hstack(
                rx.box(
                    rx.image(
                        src="/images/quique-rounded.png",
                        width="200px",
                        height="auto",
                        margin="15px",
                    ),
                    width="30%",
                ),
                rx.box(
                    rx.text(
                        f"""
                        Soc Quique Serrano, electromecànic de professió, animador infantil i juvenil per vocació i formador per a les empreses per extensió.
                        """,
                        style=styles.about_section1_text,
                    ),
                    rx.text(
                        f"""
                        Durant màs de 20 anys he exercit treballs relacionats amb la maquinària: instal·lació, manteniment i reparació en el seu vessant mecànic, elèctrica i de control. També he tingut contacte amb PLCs, d'ací el meu coneixement en programació lògica.
                        """,
                        style=styles.about_section1_text,
                    ),
                    rx.text(
                        f"""
                        En 2016, un esdeveniment inesperat em va apartar laboralment de tot eixe món. Lluny de desanimar-me, vaig decidir formar-me com a animador de temps lliure infantil i juvenil on vaig descobrir la meua vocació per l'educació. Vaig tindre el plaer de treballar en la Escoleta Matinera i en la Escoleta d'estiu en el col·legi del meu poble, el CRA El Trescaire. Allí vaig afermar els meus dots de comunicació envers els xicotets i vaig desenvolupar la meua vocació educativa.
                        """,
                        style=styles.about_section1_text,
                    ),
                    rx.text(
                        f"""
                        Posteriorment vaig obtindre el certificat de professionalitat de "Docència de la formació professional per a l'ocupació", on vaig aprendre a estructurar adequadament el contingut d'un curs i les tècniques de desenvolupament i avaluació.
                        """,
                        style=styles.about_section1_text,
                    ),
                    rx.text(
                        f"""
                        L'interés per la programació no ha decaigut i ara estic aprenent python i desenvolupament web de la mà de famosos comunicadors de la xarxa com Mouredev, DotCSV i Midudev, així com bootcamps de Google i edX.
                        """,
                        style=styles.about_section1_text,
                    ),
                    rx.text(
                        f"""
                        Al mateix temps continu desenvolupant projectes amb la plataforma Arduino i també, a poc a poc, vaig traduint al català/valencià la documentació de la plataforma. També soc col·laborador de Softcatalà com a traductor, estant involucrat actualment en la traducció del projecte gnome44.
                        """,
                        style=styles.about_section1_text,
                    ),
                    rx.text(
                        f"""
                        Com veieu, soc una persona bastant activa, preocupada per com funcionen les coses. Em motiva tindre un trencaclosques que resoldre, així que si tens una idea, per complidada que siga compta amb mi!
                        """,
                        style=styles.about_section1_text,
                    ),
                    color=Color.TEXTCOLOR.value,
                    padding_left="12px",
                    padding_right="12px",
                    width="70%",
                    
                ),
                align="center",
            ),

        ),

# Secció 2. Fora del treball

        rx.section(
            rx.center(
                rx.image(
                    src="/images/espeleo.jpg",
                    width="200px",
                    height="auto",
                    margin_top="-150px",
                    margin_bottom="20px",
                    border_radius="15px 50px",
                    border_width="15px",
                    border_style="solid",
                    border_color=Color.BACKGROUND1.value,
                ),
            ),
            rx.heading(
                "Fora del treball",
                color=Color.BACKGROUND1.value,
                font_size="40px",
                margin_bottom="10px",
            ),
            rx.text(
                f"""
                 Una ànima aventurera amb una passió desbordant per la vida a l'aire lliure i tot el que la naturalesa té per a oferir. Quan no estic solcant senderes a la recerca de noves aventures, em trobes explorant coves i cavernes com un espeleòleg intrèpid.
                """,
                style=styles.about_section1_text,
                color=Color.BACKGROUND2.value,
            ),
            rx.text(
                f"""
                 Però no penses que la meua vida és només acció i adrenalina. Per a res! També tinc el meu costat tranquil i creatiu. En el meu temps lliure, m'encanta arrancar-li concordes a la meua guitarra i deixar-me portar per la màgia de la música. Ah, i no oblides esmentar el meu amor pel menjar entre amics i en família. No hi ha res com reunir-se al voltant d'una taula plena de plats deliciosos i compartir moments inoblidables amb les persones que més vols.
                """,
                style=styles.about_section1_text,
            ),
            rx.text(
                f"""
                 Ah, i què dir del meu xicotet jardí de plantes aromàtiques? És el meu oasi de pau, on cultive i cuide amb afecte una varietat d'herbes que fan que qualsevol plat es convertisca en una experiència sensorial única.
                """,
                style=styles.about_section1_text,
            ),
            rx.text(
                f"""
                 Així que ja ho saps, si estàs buscant a algú que siga igual part aventura i naturalesa, part música i bon menjar, ací em tens! Llest per a viure cada moment al màxim i gaudir de tot el que la vida té per a oferir!
                """,
                style=styles.about_section1_text,
            ),
            style=styles.about_even_section,

        ),

# Seccio 3. Habilitats i eines

        rx.section(
            rx.heading(
                "Habilitats i Eines",
                font_size="40px",
                margin_bottom="10px",
                ),
            rx.text(
                "Les habilitats, eines i tecnologies que faig servir per donar vida als teus productes",
                font_size="24px",
                margin_bottom="20px",
                ),

# Primera fila d'icones

            rx.center(
                rx.flex(
                    rx.center(
                        rx.image(
                            src="/icons/html5.png",
                            width="100px",
                            height="auto",
                        ),
                        rx.text("HTML5"),
                        direction="column",
                    ),
                    rx.center(
                        rx.image(
                            src="/icons/css.png",
                            width="100px",
                            height="auto",
                        ),
                        rx.text("CSS3"),
                        direction="column",
                    ),
                    rx.center(
                        rx.image(
                            src="/icons/javascript.png",
                            width="100px",
                            height="auto",
                        ),
                        rx.text("JavaScript"),
                        direction="column",
                    ),
                    rx.center(
                        rx.image(
                            src="/icons/python.png",
                            width="100px",
                            height="auto",
                        ),
                        rx.text("Python"),
                        direction="column",
                    ),
                    rx.center(
                        rx.image(
                            src="/icons/reflex.png",
                            width="100px",
                            height="auto",
                        ),
                        rx.text("Reflex"),
                        direction="column",
                    ),
                    spacing="5",
                ),
            margin_top="20px",
            margin_bottom="20px",
            ),

# Segona fila d'icones

            rx.center(
                rx.flex(
                    rx.center(
                        rx.image(
                            src="/icons/git.png",
                            width="100px",
                            height="auto",
                        ),
                        rx.text("Git"),
                        direction="column",
                    ),
                    rx.center(
                        rx.image(
                            src="/icons/github.png",
                            width="100px",
                            height="auto",
                        ),
                        rx.text("GitHub"),
                        direction="column",
                    ),
                    rx.center(
                        rx.image(
                            src="/icons/ordenador.png",
                            width="100px",
                            height="auto",
                        ),
                        rx.text("Responsive"),
                        direction="column",
                    ),
                    rx.center(
                        rx.image(
                            src="/icons/wordpress.png",
                            width="100px",
                            height="auto",
                        ),
                        rx.text("Wordpress"),
                        direction="column",
                    ),
                    spacing="5",
                ),
            ),

# Atribució de les icones

            rx.center(
                rx.text(
                    "Icones obtingudes en ",
                    rx.link(
                        "flaticon", 
                        href="https://www.flaticon.es/",
                        is_external=True,
                    ),
                ),
                font_size="10px",
                margin_top="10px",
            ),
            margin_top="20px",
            margin_bottom="20px",
            style=styles.about_odd_section,
            # iconos obtenidos en flaticon
        ),
        width="100%",
)