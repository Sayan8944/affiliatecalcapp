import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(page_title="Affiliate Calculator", layout="centered")
st.title("Affiliate Revenue Calculator")

# Embed the Calconic iframe
components.html(
    """
    <iframe src="https://app.calconic.com/api/embed/calculator/68223cae68734d002aef32a0"
            sandbox="allow-same-origin allow-forms allow-scripts allow-top-navigation allow-popups-to-escape-sandbox allow-popups"
            title="Calconic Calculator"
            height="600"
            style="width: 100%; border: none;">
    </iframe>
    <script>
      (function() {
        function inViewport(element) {
          var m = 100, w = window, r = element.getBoundingClientRect(),
              wB = w.innerHeight, wR = w.innerWidth;
          return ((0 <= r.top && wB - m >= r.top)
                   || (0 >= r.top && wB <= r.bottom)
                   || (m <= r.bottom && wB >= r.bottom))
              && ((0 <= r.left && wR - m >= r.left)
                   || (0 >= r.left && wR <= r.right)
                   || (m <= r.right && wR >= r.right));
        }
        var iframes = [];
        window.addEventListener("message", function(e) {
          var pp = "https://www.paypalobjects.com/api/checkout.4.0.141.js";
          if (e.data && e.data.action === "LOAD_PAYPAL"
              && !document.querySelector('script[src="'+pp+'"]')) {
            var s = document.createElement("script");
            s.src = pp; s.async = true;
            s.dataset = {
              paypalCheckout: true,
              noBridge: true,
              state: "ppxo_meta",
              env: "production"
            };
            document.body.append(s);
          }
          if (e.data && e.data.action === "CALCONIC_UPDATE_HEIGHT") {
            var sel = 'iframe[src="https://app.calconic.com/api/embed/calculator/'
                      + e.data.payload.id + '"]';
            document.querySelectorAll(sel).forEach(function(f) {
              f.height = e.data.payload.height;
              if (!iframes.includes(f)) {
                iframes.push(f);
                var iv = setInterval(function() {
                  f.contentWindow.postMessage({action:'IS_ACTIVE'}, '*');
                  if (inViewport(f)) {
                    clearInterval(iv);
                    f.contentWindow.postMessage({action:'IN_VIEWPORT'}, '*');
                  }
                }, 200);
              }
            });
          }
        });
      })();
    </script>
    """,
    height=600,
    scrolling=False
)
