import BookCard from '../../components/book-card/BookCard';

import styles from './full-catalog.module.css'

const FullCatalog = (props) => {

    const { books } = props

    return (
        <div className={styles.wrapper}>
            <div className={styles.titleContainer}>
                <h1 className={styles.title}>Full Catalog</h1>
            </div>

            <div className={styles.bookContainer}>
                {books.map(el => (
                    <BookCard key={el.record_id} book={el}/>
                ))}
            </div>

        </div>
    );
}

export default FullCatalog;
