import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import { ThemeProvider, ColorModeProvider } from "@chakra-ui/react";
import { extendTheme } from "@chakra-ui/react";
import "./index.css";

const theme = extendTheme({
	colors: {
		bg: {
			100: "#121212",
			200: "#222222",
			300: "#232323",
			400: "#323232",
		},
		blue: {
			100: "#10add1",
		},
		white: {
			800: "#ffffff",
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
