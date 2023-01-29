import flet as ft
import time

class SignInView(ft.View):
    def __init__(self,
        route=None,
        appbar=None,
        navigation_bar=None,
        main_bgcolor='#212344',
        container_bgcolor='#181a20',
        text_color=ft.colors.WHITE,
        forgroundcolor='#5468ff',
        signin_text_color=ft.colors.WHITE,
        signin_with_google_text_color=ft.colors.BLACK,
        email_text_color=ft.colors.WHITE,
        password_text_color=ft.colors.WHITE,
        google_logo='https://pngimg.com/uploads/google/google_PNG19635.png',
        mobile=False,
        use:list=['email'],
        on_singin_clicked=None,
        on_signin_with_google_clicked=None,
        on_forgot_password_clicked=None,
        on_signup_clicked=None,
        hinter_text_color=ft.colors.WHITE30
    ):

        # references
        email = ft.Ref[ft.TextField]()
        password = ft.Ref[ft.TextField]()
        email_container = ft.Ref[ft.Container]()
        password_container = ft.Ref[ft.Container]()

        #required functions
        def signin_clicked(e):
            #validates weither both email and password fields are filled and calles the given on_singin_clicked
            if email.current.value == '':
                email_container.current.bgcolor = ft.colors.RED
                email_container.current.update()
                time.sleep(0.75)
                email_container.current.bgcolor = '#262a34'
                email_container.current.update()
                return
            elif password.current.value == '':
                password_container.current.bgcolor = ft.colors.RED
                password_container.current.update()
                time.sleep(0.75)
                password_container.current.bgcolor = '#262a34'
                password_container.current.update()
                return

            if on_singin_clicked is not None:
                e.data = [email.current.value, password.current.value]
                on_singin_clicked(e)

        def signin_with_google_clicked(e):
            #this function only exists to make the cursur pointer even if no function is defined
            if on_signin_with_google_clicked is not None:
                on_signin_with_google_clicked(e)

        #ui
        controls = [
            #Main Container
            ft.Container(

                #Main Column
                content=ft.Column([

                    #header text
                    ft.Text(
                        'Welcom Back!',
                        size=20,
                        weight=ft.FontWeight.W_500,
                        color=text_color
                    ),

                    #subheader
                    ft.Text(
                        value='please sign in to your account',
                        opacity=0.3,
                        color=text_color
                    ),

                    #spacer
                    ft.Divider(opacity=0, height=40),

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

                    #Password textfield
                    ft.Container(
                        ref=password_container,

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

                    #forgot password button

                    ft.Container(
                        content=ft.TextButton(
                            'Forgot Password?',
                            style=ft.ButtonStyle(
                                color={
                                    ft.MaterialState.DEFAULT:ft.colors.WHITE30
                                },

                                overlay_color=ft.colors.TRANSPARENT
                            ),

                            on_click=on_forgot_password_clicked
                        ),

                        alignment=ft.alignment.center_right,
                        margin=ft.margin.only(top=-15, right=20)
                    ),
                    
                    #spacer
                    ft.Divider(opacity=0, height=30),

                    #sign in button
                    ft.Container(
                        content=ft.Text('Sign In', color=signin_text_color),
                        alignment=ft.alignment.center,
                        height=60,
                        bgcolor=forgroundcolor,
                        margin=ft.margin.symmetric(horizontal=20),
                        border_radius=20,
                        on_click=signin_clicked
                    ),

                    #sign in with google button
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Image(
                                    src=google_logo,
                                    width=35,
                                    height=35,
                                    fit=ft.ImageFit.COVER,
                                ),
                                ft.Text(value='Sign In with Google', color=signin_with_google_text_color)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        bgcolor=ft.colors.WHITE,
                        height=60,
                        margin=ft.margin.symmetric(horizontal=20),
                        border_radius=20,
                        on_click=signin_with_google_clicked,
                    ),

                    #sign up button
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    "Don't have an account?",
                                    weight=ft.FontWeight.W_400,
                                    size=13.5,
                                    color=text_color,
                                ),
                                ft.TextButton(
                                    text='Sign Up',
                                    style=ft.ButtonStyle(
                                        color=forgroundcolor,
                                        overlay_color=ft.colors.TRANSPARENT,
                                        padding=ft.padding.all(0),
                                    ),
                                    on_click=on_signup_clicked
                                )
                            ],
                            spacing=0,
                            alignment=ft.MainAxisAlignment.CENTER,
                            wrap=True
                        ),
                    )
                ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                width=350,
                height=630,
                bgcolor=container_bgcolor,
                border_radius=30,
                padding=ft.padding.only(top=70, bottom=10),
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