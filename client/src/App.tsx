import React, { useState } from "react";
import "./App.css";
import {
	Heading,
	Flex,
	FormControl,
	FormLabel,
	FormErrorMessage,
	FormHelperText,
	Button,
	Input,
	toast,
} from "@chakra-ui/react";

function App() {
	const [user, setUser] = useState();
	const [loginData, setLoginData] = useState({ username: "", password: "" });
	const handleChange = (type: string, value: string) => {
		setLoginData({ ...loginData, [type]: value });
	};

	const handleSubmit = () => {
		fetch(`${process.env.API_URL}/v1/auth`, {
			body: JSON.stringify(loginData),
			credentials: "include",
		})
			.then((res) => res.json())
			.then((res) => {
				setUser(res);
				toast.notify(() => `Login successful.`);
			})
			.catch((err) => {
				console.error(`Login failed: ${err}`);
				toast.notify(() => `Login failed: ${err}!`, {
					status: "error",
				});
			});
	};

	return (
		<div className="App">
			{user ? (
				<Flex>
					<Heading>Dashboard</Heading>
				</Flex>
			) : (
				<Flex>
					<Heading>Login</Heading>

					<form className="login-form">
						<FormControl isRequired>
							<FormLabel>Username</FormLabel>
							<Input type="text" />
						</FormControl>
						<FormControl isRequired>
							<FormLabel>Password</FormLabel>
							<Input
								type="password"
								onChange={(e) =>
									handleChange("password", e.target.value)
								}
							/>
							\
						</FormControl>
						<Button
							variant="primary"
							type="submit"
							onClick={handleSubmit}
						>
							Submit
						</Button>
					</form>
				</Flex>
			)}
		</div>
	);
}

export default App;
