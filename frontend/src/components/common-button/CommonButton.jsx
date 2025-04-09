import styles from './common-button.module.css'

const CommonButton = (props) => {
    
    const { text, buttonFunction, filteredArray, setFilteredArray} = props
    return (
        <button onClick={() => {
            setFilteredArray(filteredArray.splice(0, filteredArray.length))
            buttonFunction()
        }} className={styles.commonButtom}>
            {text}
        </button>
    );
}

export default CommonButton;
