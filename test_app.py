#!/usr/bin/env python
import os
from flask import Flask, request, render_template


app = Flask('test_app')


@app.route('/')
def root():
    return render_template(
        'test_app.html', request=request, environ=os.environ
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
