import React, { useState } from "react";
import {
	Heading,
	Flex,
	FormControl,
	FormLabel,
	Button,
	Input,
	useToast,
} from "@chakra-ui/react";
import axios, { AxiosError } from "axios";

function App() {
	const [user, setUser] = useState();
	const [loginData, setLoginData] = useState({ username: "", password: "" });
	const handleChange = (type: string, value: string) => {
		setLoginData({ ...loginData, [type]: value });
	};
	const toast = useToast();

	const handleSubmit = () => {
		axios
			.post(`${process.env.REACT_APP_API_URL}/auth/`, loginData, {
				withCredentials: true,
			})
			.then((res) => {
				if (res.status !== 200) throw new Error(res.data.error);
				setUser(res.data.data);
				toast({
					title: "Login Success",
					status: "success",
					duration: 5000,
				});
			})
			.catch((err: AxiosError) => {
				console.error(`Login failed: ${err}`);
				toast({
					title: "Login Failed",
					description: err.response?.data?.error || err.message,
					status: "error",
					duration: 5000,
				});
			});
	};

	return (
		<Flex color="white" direction="column">
			{user ? (
				<Flex>
					<Heading>Dashboard</Heading>
				</Flex>
			) : (
				<Flex
					className="login-form"
					direction="column"
					pl="5"
					pt="5"
					bg="bg.300"
				>
					<Heading>Login</Heading>
					<FormControl isRequired mb="5" width="50%">
						<FormLabel>Username</FormLabel>
						<Input
							color="white.800"
							type="text"
							onChange={(e) =>
								handleChange("username", e.target.value)
							}
						/>
					</FormControl>
					<FormControl isRequired mb="5" width="50%">
						<FormLabel>Password</FormLabel>
						<Input
							color="white.800"
							type="password"
							onChange={(e) =>
								handleChange("password", e.target.value)
							}
						/>
					</FormControl>
					<FormControl mb="5" width="50%">
						<Button
							bg="blue.100"
							color="white.800"
							type="submit"
							onClick={handleSubmit}
						>
							Submit
						</Button>
					</FormControl>
				</Flex>
			)}
		</Flex>
	);
}

export default App;
