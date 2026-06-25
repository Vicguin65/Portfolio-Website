import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import App from './App';
import './index.css';
import HomePage from './pages/HomePage';
import ProjectPage from './pages/ProjectPage';
import ResumePage from './pages/ResumePage';
import ContactPage from './pages/ContactPage';
import AskTylerPage from './pages/AskTylerPage';
import MediaPage from './pages/MediaPage';
import MediaDetailPage from './pages/MediaDetailPage';
import NotFoundPage from './pages/NotFoundPage';

const router = createBrowserRouter([
  { path: '/',              element: <App /> },
  { path: '/home',          element: <HomePage /> },
  { path: '/projects',      element: <ProjectPage /> },
  { path: '/resume',        element: <ResumePage /> },
  { path: '/contact',       element: <ContactPage /> },
  { path: '/ask',           element: <AskTylerPage /> },
  { path: '/features',      element: <MediaPage /> },
  { path: '/features/:slug', element: <MediaDetailPage /> },
  { path: '*',              element: <NotFoundPage /> },
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
