import Select from 'react-select'

import styles from './common-checkbox.module.css'
import { ValueContainer } from 'react-select/animated'

const CommonCheckbox = (props) => {

    const {titleText, list, selectedOptions, handleCheckboxChange} = props

    function transformToOptions(list) {

        const filteredList = list.filter(item => item !== undefined);
      
        const options = filteredList.map(item => ({
          value: item,
          label: item
        }));
      
        return options;
      }

    const options = transformToOptions(list)

    return (
        <div className={styles.inputContainer}>
            <p className={styles.inputText}>{titleText}</p>
            <Select onChange={handleCheckboxChange} className={styles.input} options={options} value={selectedOptions} isMulti={true}/>
         </div>
    );
}

export default CommonCheckbox;
