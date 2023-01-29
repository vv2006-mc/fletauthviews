import flet as ft
import time

class NewPasswordView(ft.View):
    def __init__(self,
        route=None,
        appbar=None,
        navigation_bar=None,
        main_bgcolor='#212344',
        container_bgcolor='#181a20',
        text_color=ft.colors.WHITE,
        forgroundcolor='#5468ff',
        reset_text_color=ft.colors.WHITE,
        password_text_color=ft.colors.WHITE,
        mobile=False,
        on_reset_password_clicked=None,
        hinter_text_color=ft.colors.WHITE30
    ):

        # references
        password = ft.Ref[ft.TextField]()
        password_container = ft.Ref[ft.Container]()
        confirm_password = ft.Ref[ft.TextField]()
        confirm_password_container = ft.Ref[ft.Container]()
        error_msg = ft.Ref[ft.Text]()


        #required functions
        def on_reset_clicked(e):
            if password.current.value == '':
                password_container.current.bgcolor = ft.colors.RED
                password_container.current.update()
                time.sleep(0.75)
                password_container.current.bgcolor = '#262a34'
                password_container.current.update()
                return
            if confirm_password.current.value == '':
                confirm_password_container.current.bgcolor = ft.colors.RED
                confirm_password_container.current.update()
                time.sleep(0.75)
                confirm_password_container.current.bgcolor = '#262a34'
                confirm_password_container.current.update()
                return
            
            if password.current.value == confirm_password.current.value:
                error_msg.current.visible = False
                error_msg.current.update()
                if on_reset_password_clicked is not None:
                    e.data = password.current.value
                    on_reset_password_clicked(e)
            else:
                error_msg.current.visible = True
                error_msg.current.update()

        #ui
        controls = [
            #Main Container
            ft.Container(

                #Main Column
                content=ft.Column([

                    #header text
                    ft.Text(
                        'New Password',
                        size=20,
                        weight=ft.FontWeight.W_500,
                        color=text_color
                    ),

                    #subheader
                    ft.Text(
                        value='please enter new password to continue',
                        opacity=0.3,
                        color=text_color
                    ),

                    #spacer
                    ft.Divider(opacity=0, height=10),

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
                            can_reveal_password=True,
                        ),

                        bgcolor='#262a34',
                        border_radius=20,
                        margin=ft.margin.symmetric(horizontal=20),
                        padding=ft.padding.only(left=20, right=20, top=7.5),
                        animate=ft.animation.Animation(500, curve=ft.AnimationCurve.EASE)
                    ),


                    ft.Container(
                        ref=confirm_password_container,

                        content=ft.TextField(
                            ref=confirm_password,
                            border='none',
                            border_radius=20,
                            height=55,
                            hint_text='Confirm Password',
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

                    ft.Text(
                        ref=error_msg,
                        visible=False,
                        value='Password and Confirm password are not same',
                        color=ft.colors.RED
                    ),

                    #spacer
                    ft.Divider(opacity=0, height=10),

                    #reset password button
                    ft.Container(
                        content=ft.Text('Reset Password', color=reset_text_color),
                        alignment=ft.alignment.center,
                        height=60,
                        bgcolor=forgroundcolor,
                        margin=ft.margin.symmetric(horizontal=20),
                        border_radius=20,
                        on_click=on_reset_clicked
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
