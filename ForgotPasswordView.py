import flet as ft
import time

class ForgotPasswordView(ft.View):
    def __init__(self,
        route=None,
        appbar=None,
        navigation_bar=None,
        main_bgcolor='#212344',
        container_bgcolor='#181a20',
        text_color=ft.colors.WHITE,
        forgroundcolor='#5468ff',
        signin_text_color=ft.colors.WHITE,
        email_text_color=ft.colors.WHITE,
        mobile=False,
        use:list=['email'],
        on_reset_password_clicked=None,
        hinter_text_color=ft.colors.WHITE30
    ):

        # references
        email = ft.Ref[ft.TextField]()
        email_container = ft.Ref[ft.Container]()

        #required functions
        def on_reset_clicked(e):
            if email.current.value == '':
                email_container.current.bgcolor = ft.colors.RED
                email_container.current.update()
                time.sleep(0.75)
                email_container.current.bgcolor = '#262a34'
                email_container.current.update()
                return
            e.data = email.current.value
            if on_reset_password_clicked is not None:
                on_reset_password_clicked(e)

        #ui
        controls = [
            #Main Container
            ft.Container(

                #Main Column
                content=ft.Column([

                    #header text
                    ft.Text(
                        'Forgot Password',
                        size=20,
                        weight=ft.FontWeight.W_500,
                        color=text_color
                    ),

                    #subheader
                    ft.Text(
                        value='please enter email you use to sign in',
                        opacity=0.3,
                        color=text_color
                    ),

                    #spacer
                    ft.Divider(opacity=0, height=10),

                    #Email Textfield
                    ft.Container(
                        ref=email_container,
                        content=ft.TextField(
                            ref=email,
                            border='none',
                            border_radius=20,
                            height=55,
                            hint_text='',
                            hint_style=ft.TextStyle(size=15, color=hinter_text_color),
                            text_style=ft.TextStyle(size=15, color=email_text_color)
                        ),

                        bgcolor='#262a34',
                        border_radius=20,
                        margin=ft.margin.symmetric(horizontal=20),
                        padding=ft.padding.only(left=20, right=20, top=7.5),
                        animate=ft.animation.Animation(500, curve=ft.AnimationCurve.EASE)
                    ),

                    #reset password button
                    ft.Container(
                        content=ft.Text('Request Reset', color=signin_text_color),
                        alignment=ft.alignment.center,
                        height=60,
                        bgcolor=forgroundcolor,
                        margin=ft.margin.symmetric(horizontal=20),
                        border_radius=20,
                        on_click=on_reset_clicked
                    ),

                    #back button
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    "Remember Your Password?",
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
                                    # on_click=on_signin_clicked
                                )
                            ],
                            spacing=0,
                            alignment=ft.MainAxisAlignment.CENTER,
                            wrap=True,

                        ),
                        margin=ft.margin.only(top=-10)
                    ),


                    ft.Divider(opacity=0, height=20)

                ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                width=350,
                bgcolor=container_bgcolor,
                border_radius=30,
                padding=ft.padding.only(top=40),
            )
        ]

        if mobile == True:
            controls[0].width = None
            controls[0].height = None
        
        #checks which hinter_text to use in Email textfield
        if len(use) > 0:
            hinter_text = ''
            for i in range(len(use)):
                if use[i] == 'email':
                    if i == 0:
                        hinter_text = 'Email'
                    else:
                        hinter_text = hinter_text + ' or Email'
                
                if use[i] == 'phone':
                    if i == 0:
                        hinter_text = 'Phone Number'
                    else:
                        hinter_text = hinter_text + ' or Phone Number'

                if use[i] == 'username':
                    if i == 0:
                        hinter_text = 'Username'
                    else:
                        hinter_text = hinter_text + ' or Username'
            email.current.hint_text = hinter_text
            if len(use) > 2:
                controls.insert(0, ft.Text('use only takes 2 values at most', color=ft.colors.RED, size=15))
                email.current.hint_text = ''

        else:
            controls.insert(0, ft.Text('use only takes the values email, phone, username', color=ft.colors.RED, size=15))

        #!REQUIRED
        super().__init__(
            route=route,
            controls=controls,
            appbar=appbar,
            navigation_bar=navigation_bar,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            bgcolor=main_bgcolor,
            scroll=ft.ScrollMode.AUTO,
        )