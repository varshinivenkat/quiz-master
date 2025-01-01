import AdminDashboard from "../pages/AdminDashboard.js";
import HomePage from "../pages/HomePage.js";
import LoginPage from "../pages/LoginPage.js";
import RegisterPage from "../pages/RegisterPage.js";

const routes = [
  { path: "/", component: HomePage },
  { path: "/login", component: LoginPage },
  { path: "/register", component: RegisterPage },
  { path: "/admin_dashboard", component : AdminDashboard},
];

const router = new VueRouter({
  routes,
});

export default router;
