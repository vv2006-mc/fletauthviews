import flet as ft
from SignInView import SignInView
from SignUpView import SignUpView
from ForgotPasswordView import ForgotPasswordView
from NewPasswordView import NewPasswordView


if __name__ == '__main__':
    def main(page:ft.Page):

        mobile = False

        appbar = ft.AppBar(
            # title=ft.Container(ft.Text('Sign In'), alignment=ft.alignment.center, margin=ft.margin.only(left=240)),
            automatically_imply_leading=False,
            bgcolor=ft.colors.TRANSPARENT,
            color=ft.colors.WHITE,
            actions=[
                ft.IconButton(icon=ft.icons.PERSON, width=60, tooltip='sign in', icon_color=ft.colors.WHITE, on_click=lambda _: page.go('/signin')),
                ft.IconButton(icon=ft.icons.PERSON_ADD, width=60, tooltip='sign up', icon_color=ft.colors.WHITE, on_click=lambda _: page.go('/signup')),
                ft.IconButton(icon=ft.icons.LOCK, width=60, tooltip='forgot password', icon_color=ft.colors.WHITE, on_click=lambda _: page.go('/forgotpassword')),
                ft.IconButton(icon=ft.icons.LOCK_RESET, width=60, tooltip='reset password', icon_color=ft.colors.WHITE, on_click=lambda _: page.go('/resetpassword')),
            ]
        )

        def route_change(e):
            print("Route change:", e.route)
            page.views.clear()
            page.views.append(ft.View())
            if page.route == '/signin':
                page.views.append(
                    SignInView(route='/signin', appbar=appbar, mobile=mobile)
            )
            if page.route == '/signup':
                page.views.append(
                    SignUpView(route='/signup', appbar=appbar, mobile=mobile)
                )
            if page.route == '/forgotpassword':
                page.views.append(
                    ForgotPasswordView(route='/forgotpassword', appbar=appbar, mobile=mobile)
                )
            if page.route == '/resetpassword':
                page.views.append(
                    NewPasswordView(route='/resetpassword', appbar=appbar, mobile=mobile)
                )


        def resize(e):
            if page.window_width <= 400:
                nonlocal mobile
                mobile = True
                route = page.route
                page.go('/')
                page.go(route)
            else:
                mobile = False
                route = page.route
                page.go('/')
                page.go(route)

        page.on_route_change = route_change
        page.on_resize = resize
        page.spacing = 0
        page.go('/signin')
        # page.go(page.views[-1].route)
        # page.theme = ft.Theme(page_transitions=ft.PageTransitionTheme.FADE_UPWARDS,)
        page.update()

    ft.app(target=main,)