import { Routes, Route, Link } from "react-router-dom";
import Posts from "./pages/Posts";
import Test from "./pages/Test";

function App() {
  return (
    <div className="p-4">
      {/* Навигация */}
      <nav className="space-x-4">
        <Link to="/">Posts</Link>
        <Link to="/test">Test</Link>
      </nav>

      {/* Маршруттар */}
      <Routes>
        <Route path="/" element={<Posts />} />
        <Route path="/test" element={<Test />} />
      </Routes>
    </div>
  );
}

export default App;
