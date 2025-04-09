import FullCatalog from "../Full-catalog/FullCatalog";
import Hero from "../Hero/page"
import SearchForBook from "../Search-for-book/page"

const Main = (props) => {

    const { books } = props

    return (
        <div>
            <Hero />
            <SearchForBook books={books}/>
        </div>
    );
}

export default Main;
