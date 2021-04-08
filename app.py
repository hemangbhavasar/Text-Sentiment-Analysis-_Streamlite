import streamlit as st
import requests
from bokeh.models.widgets import Div

def main():
  
	st.title("Sentiment Analysis App")
	st.text("Built with Python and Streamlit")
	st.markdown("### [![Open Source Love svg1](https://aleen42.github.io/badges/src/github.svg)](https://github.com/hemangbhavasar/)\
	`            `![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg) ")

	input_text = st.text_area("Enter Your text here", height = 50)

	if input_text is None:
		st.warning("Enter text and Predict Sentiment")

	if st.button("Generate Sentiments"):
		if input_text is not None:
			r = requests.post(
                "https://api.deepai.org/api/sentiment-analysis",
                data = {
                            'text': input_text,
                        },
                headers = {'api-key': '8f0499fe-bf0f-455d-9f4b-3acb442b49c4'}
            )
			output = r.json()['output']
			if output[0] == 'Positive' and len(output)== 1:
				st.success('Output : {}'.format(output))
			elif output[0] == 'Negative' and len(output)== 1:
				st.error('Output : {}'.format(output))
			else:
				st.info('Output : {}'.format(output))

def footer():
	st.markdown("""
	* * *
	Built with ❤️and :coffee: by [HEMANG BHAVASAR](https://www.linkedin.com/in/hemangbhavasar/)
	""")

	if st.button('Donation'):
		js = "window.open('https://paypal.me/hemangbhavasar')"  # New tab or window
		js = "window.location.href = 'https://paypal.me/hemangbhavasar'"  # Current tab
		html = '<img src onerror="{}">'.format(js)
		div = Div(text=html)
		st.bokeh_chart(div)

if __name__== "__main__":
	main()
	footer()
