The following was translated using AI

[简体中文](README.md)  | English

This code is a demo template for the Buomo website, released as an old version.

## Usage Instructions

You need to download Python and then install the Flask library

```
pip install flask
```

After downloading the source code

### Adding Images

I won't provide images, which need to be added to static/images/Honkai_Star_Rail

For example:
 - Add landscape images to h
 - Add portrait images to s

## Previewing the Running Effect

It should look like this when I run it properly

```
PS D:\xianmu\1> python run.py
 * Serving Flask app 'run'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on <url id="cvd1861qcjqmr43a2t90" type="url" status="failed" title="" wc="0">http://127.0.0.1:5000</url> 
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 104-608-534
```

Visit <url id="cvd1861qcjqmr43a2t90" type="url" status="failed" title="" wc="0">http://127.0.0.1:5000</url> in your browser, and you should be able to access templates/index.html

If you visit the images we just added, such as:

`<url id="cvd1861qcjqmr43a2tbg" type="url" status="failed" title="" wc="0">http://127.0.0.1:5000/random_image/</url> ` + <name>

`<url id="cvd1861qcjqmr43a2tbg" type="url" status="failed" title="" wc="0">http://127.0.0.1:5000/random_image/</url>崩坏星穹铁道`

Visiting `<url id="cvd1861qcjqmr43a2tbg" type="url" status="failed" title="" wc="0">http://127.0.0.1:5000/random_image/</url>崩坏星穹铁道` directly will randomly access the `h` and `s` directories under the directory.

If you want to access the `h` or `s` directory directly, for example:

`h` directory: `<url id="cvd1861qcjqmr43a2tbg" type="url" status="failed" title="" wc="0">http://127.0.0.1:5000/random_image/</url>崩坏星穹铁道?hsp=h`

Or

`s` directory: `<url id="cvd1861qcjqmr43a2tbg" type="url" status="failed" title="" wc="0">http://127.0.0.1:5000/random_image/</url>崩坏星穹铁道?hsp=s`

## Adding More Categories

This template code can add more category directories

You can check the code in routes/image_routes.py and find:
```python
# Preset categories
CATEGORIES = {
    "崩坏星穹铁道": os.path.join(IMAGE_DIR, "Honkai_Star_Rail")
}
```

You can add more categories by referring to `"崩坏星穹铁道": os.path.join(IMAGE_DIR, "Honkai_Star_Rail")`, for example:

```python
CATEGORIES = {
    "崩坏星穹铁道": os.path.join(IMAGE_DIR, "Honkai_Star_Rail"),
    "崩坏3": os.path.join(IMAGE_DIR, "Honkai3"),
    ...
}
```

Then add the newly created category to the directory, for example, if I want to create `Honkai3`, I can refer to the way the `Honkai_Star_Rail` directory was created.
