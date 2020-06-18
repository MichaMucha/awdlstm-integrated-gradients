from voila.app import Voila


if __name__ == "__main__":
    v = Voila.launch_instance(
        ["Explainer App.ipynb", "--template=vuetify-default", "--no-browser"]
    )