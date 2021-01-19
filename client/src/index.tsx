import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import { ThemeProvider, ColorModeProvider } from "@chakra-ui/react";
import { extendTheme } from "@chakra-ui/react";

const theme = extendTheme({
	colors: {
		brand: {
			900: "#1a365d",
			800: "#153e75",
			700: "#2a69ac",
		},
	},
});

ReactDOM.render(
	<ThemeProvider theme={theme}>
		<ColorModeProvider options={{ useSystemColorMode: true }}>
			<App />
		</ColorModeProvider>
	</ThemeProvider>,
	document.getElementById("root"),
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
