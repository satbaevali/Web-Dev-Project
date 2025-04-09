import styles from './results.module.css'

import BookCard from '../../components/book-card/BookCard';

const Results = (props) => {

    const { filter } = props

    return (
        <div className={styles.wrapper}>
            {filter.map((el, index) => (
                <BookCard  index={index} key={el.record_id} book={el}/>
            ))}       
        </div>
    );
}

export default Results;
