import flet as ft
import time

class SignUpView(ft.View):
    def __init__(self,
        route=None,
        appbar=None,
        navigation_bar=None,
        main_bgcolor='#212344',
        container_bgcolor='#181a20',
        text_color=ft.colors.WHITE,
        forgroundcolor='#5468ff',
        email_text_color=ft.colors.WHITE,
        password_text_color=ft.colors.WHITE,
        mobile=False,
        on_signup_clicked=None,
        on_signin_clicked=None,
        signup_text_color=ft.colors.WHITE,
        hinter_text_color=ft.colors.WHITE30,
        email_visible = True,
        password_visible = True,
        name_visible = True,
        phone_visible = True
    ):

        # references
        email = ft.Ref[ft.TextField]()
        phone = ft.Ref[ft.TextField]()
        name = ft.Ref[ft.TextField]()
        password = ft.Ref[ft.TextField]()
        email_container = ft.Ref[ft.Container]()
        phone_container = ft.Ref[ft.Container]()
        name_container = ft.Ref[ft.Container]()
        password_container = ft.Ref[ft.Container]()

        #required code
        components = []

        if name_visible == True:
            components.append((name_container, name))
        if email_visible == True:
            components.append((email_container, email))
        if phone_visible == True:
            components.append((phone_container, phone))
        if password_visible == True:
            components.append((password_container, password))

        #required functions
        def signup_clicked(e):
            #validates weither all visible fields are filled and calles the given on_singun_clicked
            completly_filled = True
            for i in components:
                if i[1].current.value == '':
                    completly_filled = False
                    i[0].current.bgcolor = ft.colors.RED
                    i[0].current.update()
                    time.sleep(0.75)
                    i[0].current.bgcolor = '#262a34'
                    i[0].current.update()
                    break

            if on_signup_clicked is not None and completly_filled == True:
                e.data = [name.current.value, email.current.value, phone.current.value, password.current.value]
                on_signup_clicked(e)
        #ui
        controls = [
            #Main Container
            ft.Container(

                #Main Column
                content=ft.Column([

                    #header text
                    ft.Text(
                        'Create new account',
                        size=20,
                        weight=ft.FontWeight.W_500,
                        color=text_color
                    ),

                    #subheader
                    ft.Text(
                        value='please fill the form to continue',
                        opacity=0.3,
                        color=text_color
                    ),

                    #spacer
                    ft.Divider(opacity=0, height=40),

                    #Name Textfield
                    ft.Container(
                        ref=name_container,
                        visible=name_visible,
                        content=ft.TextField(
                            ref=name,
                            border='none',
                            border_radius=20,
                            height=55,
                            hint_text='Full Name',
                            hint_style=ft.TextStyle(size=15, color=hinter_text_color),
                            text_style=ft.TextStyle(size=15, color=email_text_color)
                        ),

                        bgcolor='#262a34',
                        border_radius=20,
                        margin=ft.margin.symmetric(horizontal=20),
                        padding=ft.padding.only(left=20, right=20, top=7.5),
                        animate=ft.animation.Animation(500, curve=ft.AnimationCurve.EASE)
                    ),

                    #Email Textfield
                    ft.Container(
                        ref=email_container,
                        visible=email_visible,
                        content=ft.TextField(
                            ref=email,
                            border='none',
                            border_radius=20,
                            height=55,
                            hint_text='Email',
                            hint_style=ft.TextStyle(size=15, color=hinter_text_color),
                            text_style=ft.TextStyle(size=15, color=email_text_color)
                        ),

                        bgcolor='#262a34',
                        border_radius=20,
                        margin=ft.margin.symmetric(horizontal=20),
                        padding=ft.padding.only(left=20, right=20, top=7.5),
                        animate=ft.animation.Animation(500, curve=ft.AnimationCurve.EASE)
                    ),

                    #Phone Number Textfield 
                    ft.Container(
                        ref=phone_container,
                        visible = phone_visible,
                        content=ft.TextField(
                            ref=phone,
                            border='none',
                            border_radius=20,
                            height=55,
                            hint_text='Phone Number',
                            hint_style=ft.TextStyle(size=15, color=hinter_text_color),
                            text_style=ft.TextStyle(size=15, color=email_text_color)
                        ),

                        bgcolor='#262a34',
                        border_radius=20,
                        margin=ft.margin.symmetric(horizontal=20),
                        padding=ft.padding.only(left=20, right=20, top=7.5),
                        animate=ft.animation.Animation(500, curve=ft.AnimationCurve.EASE)
                    ),

                    #Password textfield
                    ft.Container(
                        ref=password_container,
                        visible= password_visible,
                        content=ft.TextField(
                            ref=password,
                            border='none',
                            border_radius=20,
                            height=55,
                            hint_text='Password',
                            hint_style=ft.TextStyle(size=15, color=hinter_text_color),
                            text_style=ft.TextStyle(size=15, color=password_text_color),
                            password=True,
                            can_reveal_password=True
                        ),

                        bgcolor='#262a34',
                        border_radius=20,
                        margin=ft.margin.symmetric(horizontal=20),
                        padding=ft.padding.only(left=20, right=20, top=7.5),
                        animate=ft.animation.Animation(500, curve=ft.AnimationCurve.EASE)
                    ),

                    #spacer
                    ft.Divider(opacity=0, height=30),

                    #sign up button
                    ft.Container(
                        content=ft.Text('Sign Up', color=signup_text_color),
                        alignment=ft.alignment.center,
                        height=60,
                        bgcolor=forgroundcolor,
                        margin=ft.margin.symmetric(horizontal=20),
                        border_radius=20,
                        on_click=signup_clicked
                    ),

                    #sign in button
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    "Have an Account?",
                                    weight=ft.FontWeight.W_400,
                                    size=13.5,
                                    color=text_color,
                                ),
                                ft.TextButton(
                                    text='Sign In',
                                    style=ft.ButtonStyle(
                                        color=forgroundcolor,
                                        overlay_color=ft.colors.TRANSPARENT,
                                        padding=ft.padding.all(0),
                                    ),
                                    on_click=on_signin_clicked
                                )
                            ],
                            spacing=0,
                            alignment=ft.MainAxisAlignment.CENTER,
                            wrap=True,

                        ),
                    ),

                    ft.Divider(opacity=0, height=30)
                ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                width=350,
                bgcolor=container_bgcolor,
                border_radius=30,
                padding=ft.padding.only(top=70),
            )
        ]

        if mobile == True:
            controls[0].width = None
            controls[0].height = None
            # controls[0].expand = True
        
        
        #!REQUIRED
        super().__init__(
            route=route,
            controls=controls,
            appbar=appbar,
            navigation_bar=navigation_bar,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            bgcolor=main_bgcolor,
            scroll = ft.ScrollMode.AUTO,
        )