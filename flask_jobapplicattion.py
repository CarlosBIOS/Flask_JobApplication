# content="width=device-width, initial-scale=1, shrink-to-fit=no":

# `width=device-width`: This sets the width of the webpage to match the width of the device's screen. This ensures that
# the page is laid out correctly on devices with different screen sizes.

# `shrink-to-fit=no`: This is an optional setting that tells the browser not to shrink the page to fit the screen size
# if the device has a high-resolution display. This is useful for newer devices with high pixel density, where you want
# the page to be displayed at its normal size rather than being zoomed out.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
