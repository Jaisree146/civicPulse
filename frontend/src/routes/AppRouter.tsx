import { createBrowserRouter, Navigate } from "react-router-dom";

import Login from "../features/auth/Login";
import Register from "../features/auth/Register";
import ChangePassword from "../features/auth/ChangePassword";

import ProtectedRoute from "./ProtectedRoute";
import RoleRoute from "./RoleRoute";

function CitizenDashboard() {
  return <h1>Citizen Dashboard</h1>;
}

function MunicipalDashboard() {
  return <h1>Municipal Dashboard</h1>;
}

function DepartmentDashboard() {
  return <h1>Department Dashboard</h1>;
}

function Unauthorized() {
  return <h1>Unauthorized</h1>;
}

export const router = createBrowserRouter([
  {
    path: "/",
    element: <Navigate to="/login" replace />,
  },

  {
    path: "/login",
    element: <Login />,
  },

  {
    path: "/register",
    element: <Register />,
  },

  {
    element: <ProtectedRoute />,
    children: [
      {
        element: <RoleRoute allowedRoles={["Citizen"]} />,
        children: [
          {
            path: "/citizen/dashboard",
            element: <CitizenDashboard />,
          },
        ],
      },

      {
        element: (
          <RoleRoute allowedRoles={["Municipal Officer"]} />
        ),
        children: [
          {
            path: "/municipal/dashboard",
            element: <MunicipalDashboard />,
          },
        ],
      },

      {
        element: (
          <RoleRoute allowedRoles={["Department Officer"]} />
        ),
        children: [
          {
            path: "/department/dashboard",
            element: <DepartmentDashboard />,
          },
        ],
      },
    ],
  },

  {
    path: "/unauthorized",
    element: <Unauthorized />,
  },
]);