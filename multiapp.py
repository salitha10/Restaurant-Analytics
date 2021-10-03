"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
import base64

class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):

        main_bg = "bgImage1.jpg" 
        main_bg_ext = "bgImage.jpg"

        # side_bg = "background.jpg"
        # side_bg_ext = "jpg"

        st.markdown(
        f"""
        <style>
        .reportview-container {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
        }}
           
        </style>
        """,
        unsafe_allow_html=True)


#  .sidebar .sidebar-content {{
#             background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
#         }}


        # app = st.sidebar.radio(
        st.sidebar.markdown(""" # Navigation """)
        app = st.sidebar.selectbox('Select page',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()