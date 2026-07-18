import React from "react";

import ReactDOM from "react-dom/client";

import App from "./App";

import "./index.css";

import { QueryProvider } from "./providers/QueryProvider";

import { AuthProvider } from "./context/AuthContext";

import { Toaster } from "react-hot-toast";

import "./api/interceptor";

ReactDOM.createRoot(

document.getElementById("root")!

).render(

<React.StrictMode>

<QueryProvider>

<AuthProvider>


<App/>

<Toaster

position="top-right"

/>


</AuthProvider>

</QueryProvider>

</React.StrictMode>

);