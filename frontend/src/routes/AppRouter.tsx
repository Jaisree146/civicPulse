import { createBrowserRouter, Navigate } from "react-router-dom";

import Login from "../features/auth/Login";
import Register from "../features/auth/Register";


import ProtectedRoute from "./ProtectedRoute";
import RoleRoute from "./RoleRoute";

import CitizenDashboard from "../features/dashboard/citizen/Dashboard";
import MunicipalDashboard from "../features/dashboard/municipal/Dashboard";
import DepartmentDashboard from "../features/dashboard/department/Dashboard";
import DashboardLayout from "../layouts/DashboardLayout";

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
      element: <DashboardLayout />,
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
            <RoleRoute
              allowedRoles={["Municipal Officer"]}
            />
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
            <RoleRoute
              allowedRoles={["Department Officer"]}
            />
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
  ],
},

  {
    path: "/unauthorized",
    element: <Unauthorized />,
  },
]);