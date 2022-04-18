odoo.define("owl_tutorial.ControlPanel", function (require) {
    "use strict";
    const ControlPanel = require("web.ControlPanel");
    const { useState } = owl.hooks;
  
    // ConstrolPanel has a patch function thanks to the patchMixin 
    // This is the usual syntax, first argument is the name of our patch.
    ControlPanel.patch("owl_tutorial.ControlPanelCodingDodo", (T) => {
      class ControlPanelPatched extends T {
        constructor() {
          super(...arguments);
          this.state = useState({
            customText: "",
          });
          console.log(this.state);
        }
          
        async willUpdateProps(nextProps) {
          // Don't forget to call the super
          await super.willUpdateProps(nextProps);
          
          let self = this;
          fetch("https://type.fit/api/quotes")
            .then(function (response) {
              return response.json();
            })
            .then(function (data) {
              let quote = data[Math.floor(Math.random() * data.length)];
              // Update the state of the Component
              Object.assign(self.state, {
                customText: `${quote.text} - ${quote.author}`,
              });
            });
        }
      }
      return ControlPanelPatched;
    });
  });
  