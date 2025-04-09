import styles from './common-input.module.css'

const CommonInput = (props) => {

    const {titleText, list, inputValue, handleInputValue} = props

    return (
        <div className={styles.inputContainer}>
            <p className={styles.inputText}>{titleText}</p>
            <select onChange={handleInputValue} className={styles.input}>
                <option value="Any">Any</option>
                {list.map((item, index) => {
                    return(
                        <option {...props} key={index} value={item}>{item}</option>
                    )
                })}
            </select>
        </div>
    );
}

export default CommonInput;
