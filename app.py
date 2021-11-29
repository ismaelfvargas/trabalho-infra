from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from s3 import s3_upload


app = Flask(__name__)
app.config.from_object("config")

class UploadForm(FlaskForm):
    example = FileField("Example File")

@app.route("/", methods=["POST", "GET"])
def upload_page():
    form = UploadForm()
    if form.validate_on_submit():
        output = s3_upload(form.example)
        flash("{src} uploaded to S3 as {dst}".format(src=form.example.data.filename, dst=output))
    return render_template("example.html", form=form)

if __name__ == "__main__":
    app.run()
