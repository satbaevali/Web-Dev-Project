import styles from './book-card.module.css'

const BookCard = (props) => {

    const { book } = props

    return (
            <div className={styles.card}>
            <div className={styles.imageContainer}>
                <img src="/book-cover.webp" alt="Book cover" />
            </div>
            <div className={styles.bookInformation}>
                <h2 className={styles.title}>{book.title}</h2>
                <p className={styles.author}>{Array.isArray(book.author) ? book.author.join('; ') : book.author}</p>
            </div>
            </div> 
    );
}

export default BookCard;
