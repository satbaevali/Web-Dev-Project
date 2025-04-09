import { Routes, Route } from "react-router-dom"

import books from '../../backend/database.json'

import Main from "./modules/Main/Main"
import FullCatalog from "./modules/Full-catalog/FullCatalog"
import Layout from "./modules/Layout/Layout"


function App() {

  return (
    <>
        <Routes>
            <Route path="/" element={<Layout />}>
                <Route index element={<Main books={books} />}/>
                <Route path="fullcatalog" element={<FullCatalog books={books} />}/>
            </Route>
        </Routes>
    </>
  )
}

export default App
