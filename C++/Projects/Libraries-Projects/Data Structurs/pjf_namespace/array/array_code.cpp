#ifdef ARRAY

namespace pjf {

    template <typename _ArrayType>
        array<_ArrayType>::array() {
            this->array_size = 0;
            this->extended_size = this->array_size + ARRAY_GAP;

            this->arr = new(std::nothrow) _ArrayType [this->extended_size];
            if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; throw -1;}
        }





    template <typename _ArrayType>
    array<_ArrayType>::array(const std::initializer_list<_ArrayType> &init_list) {
        this->array_size = init_list.size();
        this->extended_size = this->array_size + ARRAY_GAP;

        this->arr = new(std::nothrow) _ArrayType [this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; throw -1;}
        
        for (int i=0; i<init_list.size(); ++i) {
            this->arr[i] = *(init_list.begin() + i);
        }
    }





    template <typename _ArrayType>
    array<_ArrayType>::array(const std::vector<_ArrayType> &constructing_vector) {
        this->array_size = constructing_vector.size();
        this->extended_size = this->array_size + ARRAY_GAP;

        this->arr = new(std::nothrow) _ArrayType [this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; throw -1;}

        for (int i=0; i<constructing_vector.size(); i++) {
            this->arr[i] = constructing_vector[i];
        }
    }





    template <typename _ArrayType>
    array<_ArrayType>::array(const array<_ArrayType> &constructing_array) {
        this->array_size = constructing_array.length();
        this->extended_size = this->array_size + ARRAY_GAP;

        this->arr = new(std::nothrow) _ArrayType [this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; throw -1;}

        for (int i=0; i<constructing_array.length(); i++) {
            this->arr[i] = constructing_array[i];
        }
    }





    template <typename _ArrayType>
    array<_ArrayType>::array(int total_size, const _ArrayType &value) {
        int size = (total_size > 0) ? total_size : 0;

        this->array_size = size;
        this->extended_size = this->array_size + ARRAY_GAP;

        this->arr = new(std::nothrow) _ArrayType [this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; throw -1;}

        for (int i=0; i<size; i++) {
            this->arr[i] = value; 
        }
    }





    template <typename _ArrayType>
    array<_ArrayType>::array(const std::string &constructing_string) {
        this->array_size = constructing_string.size();
        this->extended_size = this->array_size + ARRAY_GAP;

        this->arr = new(std::nothrow) _ArrayType[this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; throw -1;}

        for (int i=0; i<constructing_string.size(); i++) {
            this->arr[i] = constructing_string[i];
        }
    }





    template <typename _ArrayType>
    array<_ArrayType>::~array() {
        if (this->arr != nullptr) {
            delete[] this->arr;
        }

        this->arr = nullptr;
    }





    template <typename _ArrayType>
    _ArrayType array<_ArrayType>::get(int index) const {
        if ((index < 0) || (index > this->array_size - 1)) {
            std::cout << "Invalid Index Position." << std::endl;
            this->~array();
            throw -2;
        }

        return this->arr[index];
    }





    template <typename _ArrayType>
    typename array<_ArrayType>::iterator array<_ArrayType>::get_iter(int index) const {
        if (index > (this->array_size-1) || index < 0) {
            std::cout << "Invalid Index Position." << std::endl;
            this->~array();
            throw -2;
        }

        return this->begin() + index;
    }





    template <typename _ArrayType>
    typename array<_ArrayType>::const_iterator array<_ArrayType>::get_citer(int index) const {
        if (index > (this->array_size-1) || index < 0) {
            std::cout << "Invalid Index Position." << std::endl;
            this->~array();
            throw -2;
        }
        
        return this->cbegin() + index;
    }





    template <typename _ArrayType>
    void array<_ArrayType>::set_length(int new_size, const _ArrayType &value) {
        if (this->array_size == new_size) {
            return;
        }

        int size = (new_size > 0) ? new_size : 0;

        _ArrayType *temp = new(std::nothrow) _ArrayType[size];
        if (temp == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        int i = 0;
        while (i < this->array_size && i < size) {
            temp[i] = this->arr[i];
            ++i;
        }
        while (i < size) {
            temp[i] = value;
            ++i;
        }

        delete[] this->arr;

        this->array_size = size;
        this->extended_size = this->array_size + ARRAY_GAP;
        
        this->arr = new(std::nothrow) _ArrayType[this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        for (int i=0; i<this->array_size; ++i) {
            this->arr[i] = temp[i];
        }

        delete[] temp;
    }





    template <typename _ArrayType>
    void array<_ArrayType>::set_size(int new_extended_size) {
        if (this->extended_size == new_extended_size) {
            return;
        }

        int size = (new_extended_size > 0) ? new_extended_size : 0;

        _ArrayType *temp = new(std::nothrow) _ArrayType[size];
        if (temp == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        int i = 0;
        while (i < size && i < this->array_size) {
            temp[i] = this->arr[i];
            ++i;
        }

        delete[] this->arr;

        this->array_size = i;
        this->extended_size = (size > 0) ? size: ARRAY_GAP;

        this->arr = new(std::nothrow) _ArrayType[this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        for (int i=0; i<this->array_size; ++i) {
            this->arr[i] = temp[i];
        }

        delete[] temp;
    }




    template <typename _ArrayType>
    void array<_ArrayType>::shrink() {
        if (this->extended_size == this->array_size) {
            return;
        }

        this->extended_size = this->array_size;

        _ArrayType *temp = new(std::nothrow) _ArrayType [this->extended_size];
        if (temp == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        for (int i=0; i<this->array_size; ++i) {
            temp[i] = this->arr[i];
        }

        delete [] this->arr;

        this->arr = new(std::nothrow) _ArrayType [this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        for (int i=0; i<this->array_size; ++i) {
            this->arr[i] = temp[i];
        }

        delete [] temp;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::push_back(const _ArrayType &value) {
        if (this->array_size == this->extended_size) {
            ++this->array_size;
            this->extended_size = this->array_size + ARRAY_GAP;

            _ArrayType *temp = new(std::nothrow) _ArrayType [this->array_size];
            if (temp == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

            for (int i=0; i<this->array_size-1; i++) {
                temp[i] = this->arr[i];
            }
            temp[this->array_size - 1] = value;

            delete[] this->arr;

            this->arr = new(std::nothrow) _ArrayType [this->extended_size];
            if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}
            
            for (int i=0; i<this->array_size; i++) {
                this->arr[i] = temp[i];
            }

            delete[] temp;
        }
        else {
            this->array_size ++;
            this->arr[this->array_size - 1] = value;
        }

        return *this;
    }




    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::push_front(const _ArrayType &value) {
        if (this->array_size == this->extended_size) {
            ++this->array_size;
            this->extended_size = this->array_size + ARRAY_GAP;

            _ArrayType *temp = new(std::nothrow) _ArrayType [this->array_size];
            if (temp == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

            for (int i=0; i<this->array_size-1; ++i) {
                temp[i+1] = this->arr[i];
            }
            temp[0] = value;

            delete[] this->arr;

            this->arr = new(std::nothrow) _ArrayType [this->extended_size];
            if (this->arr== nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

            for (int i=0; i<this->array_size; ++i) {
                this->arr[i] = temp[i];
            }

            delete[] temp;
        }
        else {
            this->array_size ++;

            for (int i=this->array_size-2; i>=0; --i) {
                this->arr[i+1] = this->arr[i];
            }
            this->arr[0] = value;
        }

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::insert(int index, const _ArrayType &value) {
        if ((index > this->array_size) || (index < 0)) {
            std::cout << "Invalid index position." << std::endl;
            this->~array();
            throw -2;
        }

        if (this->array_size == this->extended_size) {
            ++this->array_size;
            this->extended_size = this->array_size + ARRAY_GAP;
            
            _ArrayType *temp = new(std::nothrow) _ArrayType[this->array_size];
            if (temp == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

            int i = 0;
            while (i < index) {
                temp[i] = this->arr[i];
                ++i;
            }
            while (i < this->array_size - 1) {
                temp[i+1] = this->arr[i];
                ++i;
            }
            temp[index] = value;

            delete[] this->arr;

            this->arr = new(std::nothrow) _ArrayType[this->extended_size];
            if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

            for (int i=0; i<this->array_size; i++) {
                this->arr[i] = temp[i];
            }

            delete[] temp;
        }
        else {
            ++this->array_size;

            for (int i=this->array_size-2; i>=index; i--) {
                this->arr[i+1] = this->arr[i];
            }
            this->arr[index] = value;
        }

        return *this;
    }





    template <typename _ArrayType> 
    array<_ArrayType> array<_ArrayType>::insert(array<_ArrayType>::iterator &position, const _ArrayType &new_value) {
        if (!this->__link_iter_to_arr(position)) {
            std::cout << "The iterator that has be passed is either is not created by the 'this' or is out of bounds." << std::endl;
            this->~array();
            throw -3;
        }

        this->insert(this->at(position), new_value);

        return *this;
    }





    template <typename _ArrayType> 
    array<_ArrayType> array<_ArrayType>::insert(array<_ArrayType>::const_iterator &position, const _ArrayType &new_value) {
        if (!this->__link_iter_to_arr(position)) {
            std::cout << "The iterator that has be passed is either is not created by the 'this' or is out of bounds." << std::endl;
            this->~array();
            throw -3;
        }

        this->insert(this->at(position), new_value);

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::extend(const array<_ArrayType> &aArray) {
        for (_ArrayType elem: aArray) {
            this->push_back(elem);
        }

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::extend(const array<_ArrayType> &aArray, int start) {
        if (start > this->array_size || start < 0) {
            std::cout << "Invalid Index Position." << std::endl;
            this->~array();
            throw -2;
        }

        _ArrayType *temp = new(std::nothrow) _ArrayType[this->array_size + aArray.length()];
        if (temp == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        int i = 0;
        int j = 0;
        while (i < start) {
            temp[i] = this->arr[i]; 
            ++i;
        }
        while (j < aArray.length()) {
            temp[j+i] = aArray[j];
            ++j;
        }
        while (i< this->array_size) {
            temp[i+j] = this->arr[i];
            ++i;
        }

        delete[] this->arr;

        this->array_size = this->array_size + aArray.length();
        this->extended_size = this->array_size + ARRAY_GAP;

        this->arr = new(std::nothrow) _ArrayType[this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        for (int i=0; i<this->array_size; i++) {
            this->arr[i] = temp[i];
        }

        delete[] temp;

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::extend(const std::vector<_ArrayType> &aVector) {
        for (_ArrayType elem: aVector) {
            this->push_back(elem);
        }

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::extend(const std::vector<_ArrayType> &aVector, int start) {
        if (start > this->length() || start < 0) {
            std::cout << "Invalid Index Position." << std::endl;
            this->~array();
            throw -1;
        }
        
        _ArrayType *temp = new(std::nothrow) _ArrayType[this->array_size + aVector.size()];
        if (temp == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        int i = 0;
        int j = 0;
        while (i < start) {
            temp[i] = this->arr[i]; 
            ++i;
        }
        while (j < aVector.size()) {
            temp[j+i] = aVector[j];
            ++j;
        }
        while (i< this->array_size) {
            temp[i+j] = this->arr[i];
            ++i;
        }

        delete[] this->arr;

        this->array_size = this->array_size + aVector.size();
        this->extended_size = this->array_size + ARRAY_GAP;

        this->arr = new(std::nothrow) _ArrayType[this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        for (int i=0; i<this->array_size; i++) {
            this->arr[i] = temp[i];
        }

        delete[] temp;

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::extend(array<_ArrayType>::iterator &start, array<_ArrayType>::iterator &end, const array<_ArrayType> &iters_object) {
        if (!iters_object.__link_iter_to_arr(start) || !iters_object.__link_iter_to_arr(end)) {
            std::cout << "The iterators that have be passed are either are not created by the 'iters_object' or are out of bounds." << std::endl;
            this->~array();
            throw -3;
        }

        int start_i = iters_object.at(start);
        int end_i = iters_object.at(end);

        if (start_i > end_i) {
            std::cout << "Invalid Iterator Position: Starting iterator must be lower than the ending one." << std::endl;
            this->~array();
            throw -2;
        }

        for (array<_ArrayType>::iterator it=start; it!=end; ++it) {
            this->push_back(*it);
        }

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::extend(array<_ArrayType>::const_iterator &start, array<_ArrayType>::const_iterator &end, const array<_ArrayType> &iters_object) {
        if (!iters_object.__link_iter_to_arr(iters_object, start) || !iters_object.__link_iter_to_arr(iters_object, end)) {
            std::cout << "The iterators that have be passed are either are not created by the 'iters_object' or are out of bounds." << std::endl;
            this->~array();
            throw -3;
        }

        int start_i = iters_object.at(start);
        int end_i = iters_object.at(end);

        if (start_i > end_i) {
            std::cout << "Invalid Iterator Position: Starting iterator must be lower than the ending one." << std::endl;
            this->~array();
            throw -2;
        }

        for (array<_ArrayType>::const_iterator it=start; it!=end; ++it) {
            this->push_back(*it);
        }

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::extend(typename std::vector<_ArrayType>::iterator &start, typename std::vector<_ArrayType>::iterator &end, std::vector<_ArrayType> &iters_object) {
        if (!this->__link_iter_to_vector(iters_object, start) || !this->__link_iter_to_vector(iters_object, end)) {
            std::cout << "The iterators that have be passed are either are not created by the 'iters_object' or are out of bounds." << std::endl;
            this->~array();
            throw -3;
        }

        int start_i = std::distance(iters_object.begin(), start);
        int end_i = std::distance(iters_object.begin(), end);

        if (start_i > end_i) {
            std::cout << "Invalid Iterator Position: Starting iterator must be lower than the ending one." << std::endl;
            this->~array();
            throw -2;
        }

        for (typename std::vector<_ArrayType>::iterator it=start; it!=end; ++it) {
            this->push_back(*it);
        }

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::extend(typename std::vector<_ArrayType>::const_iterator &start, typename std::vector<_ArrayType>::const_iterator &end, std::vector<_ArrayType> &iters_object) {
        if (!this->__link_iter_to_vector(iters_object, start) || !this->__link_iter_to_vector(iters_object, end)) {
            std::cout << "The iterators that have be passed are either are not created by the 'iters_object' or are out of bounds." << std::endl;
            this->~array();
            throw -3;
        }

        int start_i = std::distance(iters_object.cbegin(), start);
        int end_i = std::distance(iters_object.cbegin(), end);

        if (start_i > end_i) {
            std::cout << "Invalid Iterator Position: Starting iterator must be lower than the ending one." << std::endl;
            this->~array();
            throw -2;
        }

        for (typename std::vector<_ArrayType>::const_iterator it=start; it!=end; ++it) {
            this->push_back(*it);
        }

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::pop_back() {
        if (this->array_size == 0) {
            std::cout << "No elements to delete." << std::endl;
            this->~array();
            throw -5;
        }

        if (this->extended_size - this->array_size == ARRAY_GAP) {
            --this->array_size;
            this->extended_size = (this->array_size != 0) ? this->array_size: ARRAY_GAP;

            _ArrayType *temp = new(std::nothrow) _ArrayType [this->extended_size];
            if (temp == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

            for (int i=0; i<this->array_size; ++i) {
                temp[i] = this->arr[i];
            }
            delete[] this->arr;

            this->arr = new(std::nothrow) _ArrayType [this->extended_size];
            if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

            for (int i=0; i<this->array_size; ++i) {
                this->arr[i] = temp[i];
            }

            delete[] temp;
        }
        else {
            --this->array_size;
        }

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::pop_front() {
        if (this->array_size == 0) {
            std::cout << "No elements to delete." << std::endl;
            this->~array();
            throw -5;
        }

        if (this->extended_size - this->array_size == ARRAY_GAP) {
            --this->array_size;
            this->extended_size = (this->array_size != 0) ? this->array_size: ARRAY_GAP;

            _ArrayType *temp = new(std::nothrow) _ArrayType [this->array_size];
            if (temp == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

            for (int i=0; i<this->array_size; i++) {
                temp[i] = this->arr[i+1];
            }

            delete[] this->arr;

            this->arr = new(std::nothrow) _ArrayType [this->extended_size];
            if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

            for (int i=0; i<this->length(); i++) {
                this->arr[i] = temp[i];
            }

            delete[] temp;
        }
        else {
            --this->array_size;

            for (int i=0; i<this->array_size+1; ++i) {
                this->arr[i] = this->arr[i+1];
            }
        }

        return *this; 
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::clear() {
        this->array_size = 0;
        this->extended_size = ARRAY_GAP;

        delete[] this->arr;

        this->arr = new(std::nothrow) _ArrayType [this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        return *this; 
    }




    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::pop(int index, int total_pos) {
        if (index < 0 || total_pos < 0 || index + total_pos > this->array_size - 1) {
            std::cout << "Invalid Index Position." << std::endl;
            this->~array();
            throw -2;
        }
        else {
            int original_size = this->array_size;

            this->array_size -= (total_pos + 1);
            this->extended_size = this->array_size + ARRAY_GAP;
            
            _ArrayType *temp = new(std::nothrow) _ArrayType [this->array_size];
            if (temp == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

            int i = 0;
            while (i < index) {
                temp[i] = this->arr[i];
                ++i;
            }
            while (i + index + total_pos < original_size) {
                temp[i] = this->arr[i+index+total_pos];
                ++i;
            }

            delete[] this->arr;

            this->arr = new(std::nothrow) _ArrayType [this->extended_size];
            if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

            for (int i=0; i<this->array_size; ++i) {
                this->arr[i] = temp[i];
            }
            delete[] temp;
        }

        return *this; 
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::remove(const _ArrayType &value, bool dupl) {
        _ArrayType *temp = new(std::nothrow) _ArrayType [this->array_size];
        if (temp == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        int j = 0;
        if (dupl) {
            for (int i=0; i<this->array_size; ++i) {
                if (this->arr[i] != value) {
                    temp[j++] = this->arr[i];
                }
            }
        }
        else {
            int i = 0;
            while (i < this->array_size && this->arr[i] != value){
                temp[j++] = this->arr[i++];
            }
            for (int k=i+1; k<this->array_size; ++k) {
                temp[j++] = this->arr[k];
            }
        }

        delete[] this->arr;

        this->array_size = j;
        this->extended_size = this->array_size + ARRAY_GAP;

        this->arr = new(std::nothrow) _ArrayType [this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        for (int i=0; i<this->array_size; ++i) {
            this->arr[i] = temp[i];
        }

        delete[] temp;


        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::remove(const array<_ArrayType> &arr, bool dupl) {
        _ArrayType *temp = new(std::nothrow) _ArrayType [this->array_size];
        if (temp == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        for (int i=0; i<this->array_size; ++i) {
            temp[i] = this->arr[i];
        }

        int temp_size = this->array_size;
        int k;
        if (dupl) {
            for(int i=0; i<arr.length(); ++i) {
                k = 0;
                for (int j=0; j<temp_size; ++j) {
                    if (temp[j] != arr[i]) {
                        temp[k++] = temp[j];
                    }
                }
                temp_size = k;
            }
        }
        else {
            for (int i=0; i<arr.length(); ++i) {
                int j = 0;
                while (j < temp_size && temp[j] != arr[i]){
                    ++j;
                }
                k = j;
                for (int p=j; p<temp_size-1; ++p) {
                    temp[p] = temp[p+1];
                    ++k;
                }
                temp_size = k;
            }
        }

        delete[] this->arr;

        this->array_size = k;
        this->extended_size = this->array_size + ARRAY_GAP;

        this->arr = new(std::nothrow) _ArrayType [this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        for (int i=0; i<this->array_size; ++i) {
            this->arr[i] = temp[i];
        }

        delete[] temp;
        
        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::remove(const std::vector<_ArrayType> &vect, bool dupl) {
        _ArrayType *temp = new(std::nothrow) _ArrayType [this->array_size];
        if (temp == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        for (int i=0; i<this->array_size; ++i) {
            temp[i] = this->arr[i];
        }

        int temp_size = this->array_size;
        int k;
        if (dupl) {
            for(int i=0; i<vect.size(); ++i) {
                k = 0;
                for (int j=0; j<temp_size; ++j) {
                    if (temp[j] != vect[i]) {
                        temp[k++] = temp[j];
                    }
                }
                temp_size = k;
            }
        }
        else {
            for (int i=0; i<vect.size(); ++i) {
                int j = 0;
                while (j < temp_size && temp[j] != vect[i]){
                    ++j;
                }
                k = j;
                for (int p=j; p<temp_size-1; ++p) {
                    temp[p] = temp[p+1];
                    ++k;
                }
                temp_size = k;
            }
        }

        delete[] this->arr;

        this->array_size = k;
        this->extended_size = this->array_size + ARRAY_GAP;

        this->arr = new(std::nothrow) _ArrayType [this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        for (int i=0; i<this->array_size; ++i) {
            this->arr[i] = temp[i];
        }

        delete[] temp;
        
        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::pop(array<_ArrayType>::iterator &position) {
        if (!this->__link_iter_to_arr(position)) {
            std::cout << "The iterator that has be passed is either is not created by the 'this' or is out of bounds." << std::endl;
            this->~array();
            throw -3;
        }

        this->pop(this->at(position), 0);

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::pop(array<_ArrayType>::iterator &start, array<_ArrayType>::iterator &end) {
        if (!this->__link_iter_to_arr(start) || !this->__link_iter_to_arr(end)) {
            std::cout << "The iterators that have be passed ar either are not created by the 'this' or is out of bounds." << std::endl;
            this->~array();
            throw -3;
        }

        int start_i = this->at(start);
        int end_i = this->at(end);

        if (start_i > end_i) {
            std::cout << "Invalid Iterator Position: Starting iterator must be lower than the ening one." << std::endl;
            this->~array();
            exit(0);
        }

        this->pop(start_i, (end_i-start_i-1));

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::pop(array<_ArrayType>::const_iterator &start, array<_ArrayType>::const_iterator &end) {
        if (!this->__link_iter_to_arr(start) || !this->__link_iter_to_arr(end)) {
            std::cout << "The iterators that have be passed ar either are not created by the 'this' or is out of bounds." << std::endl;
            this->~array();
            throw -3;
        }

        int start_i = this->at(start);
        int end_i = this->at(end);

        if (start_i > end_i) {
            std::cout << "Invalid Iterator Position: Starting iterator must be lower than the ening one." << std::endl;
            this->~array();
            exit(0);
        }

        this->pop(start_i, (end_i-start_i-1));

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::pop(array<_ArrayType>::const_iterator &position) {
        if (!this->__link_iter_to_arr(position)) {
            std::cout << "The iterator that has be passed is either is not created by the 'this' or is out of bounds." << std::endl;
            this->~array();
            throw -3;
        }

        this->pop(this->at(position), 0);

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::delete_dupls() {
        _ArrayType *temp = new(std::nothrow) _ArrayType [this->array_size];
        if (temp == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        for (int i=0; i<this->array_size; ++i) {
            temp[i] = this->arr[i];
        }

        int k;
        int dupls = 0;
        int p = 0;
        for (int i=0; i<this->array_size-dupls; ++i) {
            k = i + 1;
            for (int j=i+1; j<this->array_size-dupls; j++) {
                if (temp[i] != temp[j]) {
                    temp[k++] = temp[j];
                }
                else {
                    ++p;
                }
            }
            dupls = p;
        }

        delete[] this->arr;

        this->array_size = k;
        this->extended_size = this->array_size + ARRAY_GAP;

        this->arr = new(std::nothrow) _ArrayType [this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        for (int i=0; i<this->array_size; ++i) {
            this->arr[i] = temp[i];
        }

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::set() {
        this->sort();
        this->delete_dupls();

        return *this; 
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::sort(int sorting_alg, bool rev) {
        switch (sorting_alg) {
            case 0:
                this->selection_sort(rev);
                break;
            case 1:
                this->bubble_sort(rev);
                break;
            case 2:
                this->insertion_sort(rev);
                break;
            case 3:
                this->improved_selection_sort(rev);
                break;
            default:
                std::cout << "Invalid Option: Allowed is 0-3." << std::endl;
                this->~array();
                throw -6;
        }

        return *this; 
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::rev_array() {
        for (int i=0; i<this->array_size/2; i++) {
            _ArrayType temp = arr[i];
            arr[i] = arr[this->array_size-1-i];
            arr[this->array_size-1-i] = temp;
        }

        return *this; 
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::rev_array(array<_ArrayType>::iterator &start, array<_ArrayType>::iterator &end) {
        if (!this->__link_iter_to_arr(start) || !this->__link_iter_to_arr(end)) {
            std::cout << "The iterators that have be passed are either are not created by the 'this' or is out of bounds." << std::endl;
            this->~array();
            throw -5;
        }

        int start_i = this->at(start);
        int end_i = this->at(end);

        if (start_i > end_i) {
            std::cout << "Invalid Iterator Position: Starting iterator must be lower than the ening one." << std::endl;
            this->~array();
            throw -2;
        }
        
        array<_ArrayType> temp = this->slice(start_i, end_i);
        temp.rev_array();

        int j = 0;
        for (int i=0; i<this->array_size; ++i) {
            if (i >= start_i && i < end_i) {
                this->arr[i] = temp[j++];
            }
        }
    
        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::rev_array(array<_ArrayType>::const_iterator &start, array<_ArrayType>::const_iterator &end) {
        if (!this->__link_iter_to_arr(start) || !this->__link_iter_to_arr(end)) {
            std::cout << "The iterators that have be passed are either are not created by the 'this' or is out of bounds." << std::endl;
            this->~array();
            throw -5;
        }

        int start_i = this->at(start);
        int end_i = this->at(end);

        if (start_i > end_i) {
            std::cout << "Invalid Iterator Position: Starting iterator must be lower than the ening one." << std::endl;
            this->~array();
            throw -2;
        }
        
        array<_ArrayType> temp = this->slice(start_i, end_i);
        temp.rev_array();

        int j = 0;
        for (int i=0; i<this->array_size; ++i) {
            if (i >= start_i && i < end_i) {
                this->arr[i] = temp[j++];
            }
        }
        
        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::shuffle() {
        array<int> new_indexes = this->__new_indexes();

        for (int i=0; i<this->array_size; ++i) {
            _ArrayType temp = this->arr[i];
            this->arr[i] = this->arr[new_indexes[i]];
            this->arr[new_indexes[i]] = temp;
        }

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::copy(const array<_ArrayType> &ob) {
        *this = ob;

        return *this; 
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::copy(const array<_ArrayType> &ob, int start_i, int end_i) {
        if (start_i < 0 || end_i < 0 || end_i > ob.length() || start_i > end_i) {
            std::cout << "Invalid Index Position." << std::endl;
            this->~array();
            throw -2;
        }

        *this = ob.slice(start_i, end_i);

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::copy(const std::vector<_ArrayType> &ob) {
        *this = ob;

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::copy(const std::vector<_ArrayType> &ob, int start_i, int end_i) {
        if (start_i < 0 || end_i < 0 || end_i > ob.size() || start_i > end_i) {
            std::cout << "Invalid Index Position." << std::endl;
            this->~array();
            throw -2;
        }

        _ArrayType *temp = new(std::nothrow) _ArrayType[ob.size()];
        if (temp == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        int j = 0;
        for (int i=start_i; i<end_i; ++i) {
            temp[j++] = ob[i];
        }

        delete[] this->arr;

        this->array_size = j;
        this->extended_size = this->array_size + ARRAY_GAP;

        this->arr = new(std::nothrow) _ArrayType[this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        for (int i=0; i<this->array_size; ++i) {
            this->arr[i] = temp[i];
        }

        delete[] temp;

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::copy(array<_ArrayType>::iterator &start, array<_ArrayType>::iterator &end, const array<_ArrayType> &iters_object) {
        int start_i = iters_object.at(start);
        int end_i = iters_object.at(end);

        if ((start_i == -1) || (end_i == -1)) {
            std::cout << "Invalid Iterator Position: Iterator out of bounds." << std::endl;
            this->~array();
            throw -2;
        }
        else if (start_i > end_i) {
            std::cout << "Invalid Iterator Position: Starting iterator must be lower than the ening one." << std::endl;
            this->~array();
            throw -2;
        }

        this->copy(iters_object.slice(start_i, end_i));

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::copy(array<_ArrayType>::const_iterator &start, array<_ArrayType>::const_iterator &end, const array<_ArrayType> &iters_object) {
        int start_i = iters_object.at(start);
        int end_i = iters_object.at(end);

        if ((start_i == -1) || (end_i == -1)) {
            std::cout << "Invalid Iterator Position: Iterator out of bounds." << std::endl;
            this->~array();
            throw -2;
        }
        else if (start_i > end_i) {
            std::cout << "Invalid Iterator Position: Starting iterator must be lower than the ening one." << std::endl;
            this->~array();
            throw -2;
        }

        this->copy(iters_object.slice(start_i, end_i));

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::copy(typename std::vector<_ArrayType>::iterator &start, typename std::vector<_ArrayType>::iterator &end, std::vector<_ArrayType> &iters_object) {
        int start_i = std::distance(iters_object.begin(), start);
        int end_i = std::distance(iters_object.begin(), end);

        if (start_i > end_i) {
            std::cout << "Invalid Iterator Position: Starting iterator must be lower than the ening one." << std::endl;
            this->~array();
            throw -2; 
        }
        else if ((start_i > iters_object.size()) || (end_i > iters_object.size())) {
            std::cout << "Invalid Iterator Position: Iterator out of bounds." << std::endl;
            this->~array();
            throw -2;
        }

        delete[] this->arr;
        
        this->array_size = end_i - start_i;
        this->extended_size = this->length() + ARRAY_GAP;

        this->arr = new(std::nothrow) _ArrayType[this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        int j = 0;
        for (int i=0; i<iters_object.size(); ++i) {
            if (i >= start_i && i < end_i) {
                this->arr[j++] = iters_object[i];
            }
        }

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::copy(typename std::vector<_ArrayType>::const_iterator &start, typename std::vector<_ArrayType>::const_iterator &end, std::vector<_ArrayType> &iters_object) {
        int start_i = std::distance(iters_object.cbegin(), start);
        int end_i = std::distance(iters_object.cbegin(), end);

        if (start_i > end_i) {
            std::cout << "Invalid Iterator Position: Starting iterator must be lower than the ening one." << std::endl;
            this->~array();
            throw -2;
        }
        else if ((start_i > iters_object.size()) || (end_i > iters_object.size())) {
            std::cout << "Invalid Iterator Position: Iterator out of bounds." << std::endl;
            this->~array();
            throw -2;
        }

        delete[] this->arr;
        
        this->array_size = end_i - start_i;
        this->extended_size = this->array_size + ARRAY_GAP;

        this->arr = new(std::nothrow) _ArrayType[this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        int j = 0;
        for (int i=0; i<iters_object.size(); ++i) {
            if (i >= start_i && i < end_i) {
                this->arr[j++] = iters_object[i];
            }
        }

        return *this;
    }





    template <typename _ArrayType>
    std::vector<_ArrayType> array<_ArrayType>::to_vector() const {
        std::vector<_ArrayType> v;
        for (int i=0; i<this->array_size; ++i) {
            v.push_back(this->arr[i]);
        }

        return v;
    }





    template <typename _ArrayType>
    const std::vector<_ArrayType> array<_ArrayType>::to_cvector() const {
        std::vector<_ArrayType> temp;
        for (int i=0; i<this->array_size; ++i) {
            temp.push_back(this->arr[i]);
        }

        const std::vector<_ArrayType> v = temp;

        return v;
    }





    template <typename _ArrayType>
    const array<_ArrayType> array<_ArrayType>::to_carray() const {
        const array<_ArrayType> arr = *this;

        return arr;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::invoke(_ArrayType (*funct)(_ArrayType)) {
        for (int i=0; i<this->array_size; i++) {
            this->arr[i] = funct(this->arr[i]);
        }

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::filter(bool (*funct)(_ArrayType)) {
        _ArrayType *temp = new(std::nothrow) _ArrayType[this->array_size];
        if (temp == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        int j = 0;
        for (int i=0; i<this->array_size; ++i) {
            if (funct(this->arr[i])) {
                temp[j++] = this->arr[i];
            }
        }

        delete[] this->arr;

        this->array_size = j;
        this->extended_size = this->array_size + ARRAY_GAP;

        this->arr = new(std::nothrow) _ArrayType[this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        for (int i=0; i<this->array_size; ++i) {
            this->arr[i] = temp[i];
        }

        delete[] temp;

        return *this;
    }





    template <typename _ArrayType>
    int array<_ArrayType>::count(const _ArrayType value) const {
        int count_var = 0;

        for (int i=0; i<this->array_size; ++i) {
            if (this->arr[i] == value) {
                ++count_var;
            }
        }

        return count_var; 
    }





    template <typename _ArrayType>
    int array<_ArrayType>::index(const _ArrayType &value) const {
        int index_var = -1;

        for (int i=0; i<this->array_size; ++i) {
            if (this->arr[i] == value) {
                index_var = i;
                break;
            }
        }

        return index_var;
    }





    template <typename _ArrayType>
    int array<_ArrayType>::index(const _ArrayType &value, int start, int end, int step) const {
        if (step > 0) {
            if (start >= 0 && end <= this->array_size && start < end) {
                for (int i=start; i<end; i+=step) {
                    if (this->arr[i] == value) {
                        return i;
                    }
                }
            }
        }
        else if (step < 0) {
            if (end >= 0 && start < this->array_size && start > end) {
                for (int i=start; i>=end; i+=step) {
                    if (this->arr[i] == value) {
                        return i;
                    }
                }
            }
        }

        return -1;
    }





    template <typename _ArrayType>
    int array<_ArrayType>::index(const array<_ArrayType> &ob) const {
        if (ob.length() * this->array_size == 0 || ob.length() > this->array_size) {
            return -1;
        }

        for (int i=0; i<this->array_size; i++) {
            if (ob == this->slice(i, i+ob.length())) {
                return i;
            }
        }

        return -1;
    }





    template <typename _ArrayType>
    int array<_ArrayType>::index(const std::vector<_ArrayType> &ob) const {
        if (ob.size() * this->array_size == 0 || ob.size() > this->array_size) {
            return -1;
        }

        for (int i=0; i<this->array_size; i++) {
            if (this->slice(i, i+ob.size()) == ob) {
                return i;
            }
        }

        return -1;
    }





    template <typename _ArrayType>
    array<int> array<_ArrayType>::indexes(const _ArrayType &value) const {
        array<int> indexes_array;

        for (int i=0; i<this->array_size; i++) {
            if (this->arr[i] == value) {
                indexes_array.push_back(i);
            }
        }

        return indexes_array;
    }





    template <typename _ArrayType>
    array<int> array<_ArrayType>::indexes(const array<_ArrayType> &ob) const {
        array<int> temp;

        if (ob.length() * this->array_size == 0 || ob.length() > this->array_size) {
            return temp;
        }

        for (int i=0; i<this->array_size; i++) {
            if (this->slice(i, i+ob.length()) == ob) {
                temp.push_back(i);
            }
        }

        return temp;
    }





    template <typename _ArrayType>
    array<int> array<_ArrayType>::indexes(const std::vector<_ArrayType> &ob) const {
        array<int> temp;

        if (ob.size() * this->array_size == 0 || ob.size() > this->array_size) {
            return temp;
        }

        for (int i=0; i<this->array_size; i++) {
            if (this->slice(i, i+ob.size()) == ob) {
                temp.push_back(i);
            }
        }

        return temp;
    }





    template <typename _ArrayType>
    int array<_ArrayType>::last_index(const _ArrayType &value) const {
        array<int> indexes = this->indexes(value);

        if (indexes.length() != 0) {
            return indexes.get(indexes.length() - 1);
        }
        return -1;
    }





    template <typename _ArrayType>
    int array<_ArrayType>::last_index(const array<_ArrayType> &ob) const {
        array<int> indexes = this->indexes(ob);

        return (indexes.length() != 0) ? indexes[indexes.length() - 1] : -1;
    }





    template <typename _ArrayType>
    int array<_ArrayType>::last_index(const std::vector<_ArrayType> &ob) const {
        array<int> indexes = this->indexes(ob);

        return (indexes.length() != 0) ? indexes[indexes.length() - 1] : -1;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::swap(int first_index, int second_index) {
        if ((first_index <= this->array_size - 1 && first_index >= 0) && (second_index >= 0 && second_index <= this->array_size - 1)) {
            _ArrayType temp = this->arr[first_index];
            this->arr[first_index] = this->arr[second_index];
            this->arr[second_index] = temp;
        }
        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::swap(array<_ArrayType>::iterator &first, array<_ArrayType>::iterator &second) {
        if (!iter_link_to_array(*this, first) || !iter_link_to_array(*this, second)) {
            std::cout << "The iterators that have be passed are either are not created by the 'this' or is out of bounds." << std::endl;
            this->~array();
            throw -5;
        }

        this->swap(this->at(first), this->at(second));

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::swap(array<_ArrayType>::const_iterator &first, array<_ArrayType>::const_iterator &second) {
        if (!iter_link_to_array(*this, first) || !iter_link_to_array(*this, second)) {
            std::cout << "The iterators that have be passed are either are not created by the 'this' or is out of bounds." << std::endl;
            this->~array();
            throw -5;
        }

        this->swap(this->at(first), this->at(second));

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::slice(int start, int end, int step) const {
        array<_ArrayType> arr;
    
        if (step > 0) {
            if (start >= 0 && end <= this->length() && start < end) {
                for (int i=start; i<end; i+=step) {
                    arr.push_back(this->get(i));
                }
            }
        }
        else if (step < 0) {
            if (end >= 0 && start < this->length() && start > end) {
                for (int i=start; i>=end; i+=step) {
                    arr.push_back(this->get(i));
                }
            }
        }

        return arr;
    }





    template <typename _ArrayType>
    std::string array<_ArrayType>::join(const std::string &seperator) const {
        std::string ret_str;
        for (int i=0; i<this->length(); i++) {
            if (i != (this->length()-1)) {
                ret_str += std::to_string(this->arr[i]);
                ret_str += seperator;
            }
            else {
                ret_str += std::to_string(this->arr[i]);
            }
        }

        return ret_str;
    }





    template <typename _ArrayType>
    std::string array<_ArrayType>::join(char seperator) const {
        std::string ret_str;
        for (int i=0; i<this->length(); i++) {
            if (i != (this->length()-1)) {
                ret_str += std::to_string(this->arr[i]);
                ret_str += seperator;
            }
            else {
                ret_str += std::to_string(this->arr[i]);
            }
        }

        return ret_str;
    }





    template <typename _ArrayType>
    bool array<_ArrayType>::is_symmetric() const {
        array<_ArrayType> temp = *this;

        for (int i=0; i<this->array_size; ++i) {
            if (this->arr[i] != this->arr[this->array_size - i - 1]) {
                return false;
            }
        }

        return true;
    }





    template <typename _ArrayType>
    bool array<_ArrayType>::is_inside(const _ArrayType &vlue) const {
        for (int i=0; i<this->array_size; ++i) {
            if (this->arr[i] == *vlue) {
                return true;
            }
        }

        return false;
    }





    template <typename _ArrayType>
    array<_ArrayType> &array<_ArrayType>::operator=(const array<_ArrayType> &left) { 
        if (this != &left) {
            delete [] this->arr;

            this->array_size = left.length();
            this->extended_size = left.size();

            this->arr = new(std::nothrow) _ArrayType [this->extended_size];
            if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

            for (int i=0; i<this->array_size; ++i) {
                this->arr[i] = left.arr[i];
            }
        }

        return *this; 
    }





    template <typename _ArrayType>
    array<_ArrayType> &array<_ArrayType>::operator=(const std::vector<_ArrayType> &ob) {
        delete [] this->arr;

        this->array_size = ob.size();
        this->extended_size = ob.capacity();

        this->arr = new(std::nothrow) _ArrayType [this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        for (int i=0; i<this->array_size; i++) {
            this->arr[i] = ob[i];
        }

        return *this; 
    }





    template <typename _ArrayType>
    bool array<_ArrayType>::operator==(const array<_ArrayType> &left) const {
        if (this->length() != left.length()) {
            return false;
        }

        for (int i=0; i<this->length(); i++) {
            if (this->arr[i] != left.arr[i]) {
                return false;
            }
        }

        return true;
    }





    template <typename _ArrayType>
    bool array<_ArrayType>::operator==(const std::vector<_ArrayType> &left) const {
        if (this->length() != left.size()) {
            return false;
        }

        for (int i=0; i<this->length(); i++) {
            if (this->arr[i] != left[i]) {
                return false;
            }
        }

        return true;
    }





    template <typename _ArrayType>
    _ArrayType &array<_ArrayType>::operator[](const int index) {
        if (index < 0 || index > (this->length()-1)) {
            std::cout << "Invalid Index Position." << std::endl;
            throw -2;
        } 

        return this->arr[index];
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::operator+=(int value) {
        if (value <= 0) {
            std::cout << "Given value must be bigger than 0." << std::endl;
            this->~array();
            exit(0);
        }
        else {
            _ArrayType *temp = new(std::nothrow) _ArrayType[this->array_size + value];
            if (temp == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

            char template_type = *typeid(temp[0]).name(); // Getting the type of _ArrayType.
            std::string type;

            if (template_type == 'i') {
                type = "int";
            }
            else if (template_type == 's') {
                type = "short int";
            }
            else if (template_type == 'l') {
                type = "long int";
            }
            else if (template_type == 'x') {
                type = "long long int";
            }
            else if (template_type == 'y') {
                type = "unsigned long long int";
            }
            else if (template_type == 'm') {
                type = "unsigned long int";
            }
            else if (template_type == 't') {
                type = "unsigned short int";
            }
            else if (template_type == 'j') {
                type = "unsigned int";
            }
            else if (template_type == 'f') {
                type = "float";
            }
            else if (template_type == 'd') {
                type = "double";
            }
            else if (template_type == 'e') {
                type = "long double";
            }
            else if (template_type == 'c') {
                type = "char";
            }
            else if (template_type == 'b') {
                type = "bool";
            }
            else if (template_type == 'N') {
                type = "string";
            }
            else {
                std::cout << "No such type supported." << std::endl;
                this->~array();
                throw -6;
            }

            for (int i=0; i<this->array_size+value; ++i) {
                if (i >= this->array_size) {
                    if (type == "string" || type == "char") {
                        temp[i] = '_';
                    }
                    else {
                        temp[i] = ' ' - 32;
                    }
                }
                else {
                    temp[i] = this->arr[i];
                }
            }

            delete[] this->arr;

            this->array_size += value;
            this->extended_size = this->array_size + ARRAY_GAP;

            this->arr = new(std::nothrow) _ArrayType[this->extended_size];
            if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

            for (int i=0; i<this->array_size; ++i) {
                this->arr[i] = temp[i];
            }

            delete[] temp;
        }

        return *this; 
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::operator+=(const array<_ArrayType> &right) {
        *this = this->extend(right);

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::operator+=(const std::vector<_ArrayType> &right) {
        *this = this->extend(right);

        return *this; 
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::operator-=(int total_indexes) {
        int size = (this->array_size - total_indexes > 0) ? this->array_size - total_indexes: 0;
        
        _ArrayType *temp = new(std::nothrow) _ArrayType [size];
        if (temp == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        for (int i=0; i<size; ++i) {
            temp[i] = this->arr[i];
        }

        delete[] this->arr;

        this->array_size = size;
        this->extended_size = this->array_size + ARRAY_GAP;

        this->arr = new(std::nothrow) _ArrayType [this->extended_size];
        if (this->arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->~array(); throw -1;}

        for (int i=0; i<this->array_size; ++i) {
            this->arr[i] = temp[i];
        }

        delete[] temp;

        return *this; 
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::operator-=(const array<_ArrayType> &right) {
        if (*this == right) {
            return *this;
        }

        this->remove(right, false);

        return *this; 
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::operator-=(const std::vector<_ArrayType> &right) {
        if (*this == right) {
            return *this;
        }

        this->remove(right, false);

        return *this;  
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::operator*=(int total_copies) {
        if (total_copies < 0) {
            std::cout << "Negative values are not accepted." << std::endl;
            this->~array();
            throw -7;
        }
        else if (total_copies == 0) {
            this->clear();
        }
        else {
            int original_size = this->length();
            for (int i=0; i<total_copies - 1; i++) {
                for (int j=0; j<original_size; j++) {
                    this->push_back(this->arr[j]);
                }
            }
        }

        return *this; 
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::operator+(const _ArrayType value) const {
        array<_ArrayType> temp = *this;
        
        return temp.push_back(value);
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::operator+(const array<_ArrayType> &right) const {
        array<_ArrayType> temp = *this;

        return temp.extend(right);
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::operator+(const std::vector<_ArrayType> &right) const {
        array<_ArrayType> temp = *this;

        return temp.extend(right);
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::operator-(int value) const {
        array<_ArrayType> temp = *this;

        if (value > temp.length()) {
            std::cout << "No such elements to delete." << std::endl;
            this->~array();
            throw -8;
        }

        for (int i=0; i<value; i++) {
            temp.pop_back();
        }

        return temp;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::operator-(const array<_ArrayType> &right) const {
        array<_ArrayType> temp = *this;

        return (temp -= right);
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::operator-(const std::vector<_ArrayType> &right) const {
        array<_ArrayType> temp = *this;

        return (temp -= right);
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::operator*(int value) const {
        array<_ArrayType> temp = *this;

        return (temp *= value);
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::operator++(int) {
        (*this) += 1;

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::operator++() {
        (*this) ++;

        for (int i=0; i<this->length(); i++) {
            _ArrayType temp = this->arr[i];
            this->arr[i] = this->arr[this->length() - 1];
            this->arr[this->length() - 1] = temp;
        }

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::operator--(int) {
        if (this->array_size == 0) {
            std::cout << "Array is empty." << std::endl;
            this->~array();
            throw -2;
        }
        this->pop_back();

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::operator--() {
        if (this->array_size == 0) {
            std::cout << "Array is empty." << std::endl;
            this->~array();
            throw -2;
        }
        this->pop_front();

        return *this;
    }





    template <typename _ArrayType>
    typename array<_ArrayType>::iterator array<_ArrayType>::begin() const {
        return iterator(this->arr);
    }





    template <typename _ArrayType>
    typename array<_ArrayType>::iterator array<_ArrayType>::end() const {
        return iterator(this->arr + this->length());
    }





    template <typename _ArrayType>
    typename array<_ArrayType>::iterator array<_ArrayType>::rbegin() const {
        return iterator(this->arr + this->length() - 1);
    }





    template <typename _ArrayType>
    typename array<_ArrayType>::iterator array<_ArrayType>::rend() const {
        return iterator(this->arr - 1);
    }





    template <typename _ArrayType>
    const typename array<_ArrayType>::const_iterator array<_ArrayType>::cbegin() const {
        return const_iterator(this->arr);
    }





    template <typename _ArrayType>
    const typename array<_ArrayType>::const_iterator array<_ArrayType>::cend() const {
        return const_iterator(this->arr + this->length());
    }





    template <typename _ArrayType>
    const typename array<_ArrayType>::const_iterator array<_ArrayType>::crbegin() const {
        return const_iterator(this->arr + this->length() - 1);
    }





    template <typename _ArrayType>
    const typename array<_ArrayType>::const_iterator array<_ArrayType>::crend() const {
        return const_iterator(this->arr - 1);
    }





    template <typename _ArrayType>
    int array<_ArrayType>::at(array<_ArrayType>::iterator &it) const {
        for (int i=0; i<this->array_size; i++) {
            if (it == (this->begin()+i)) {
                return i;
            }
        }

        return -1;
    }





    template <typename _ArrayType>
    int array<_ArrayType>::at(array<_ArrayType>::const_iterator &it) const {
        for (int i=0; i<this->array_size; i++) {
            if (it == (this->begin()+i)) {
                return i;
            }
        }

        return -1;
    }





    template <typename _ArrayType>
    bool array<_ArrayType>::__common_iterator::operator!=(const array<_ArrayType>::__common_iterator &element) const {
        if (this->current != element.current) {
            return true;
        }
        return false;
    }






    template <typename _ArrayType>
    bool array<_ArrayType>::__common_iterator::operator==(const array<_ArrayType>:: __common_iterator &element) const {
        if (*this != element) {
            return false;
        }
        return true;
    }





    template <typename _ArrayType>
    bool array<_ArrayType>::__common_iterator::operator>(const array<_ArrayType>::__common_iterator &_it) const {
        return (this->current > _it.current) ? true : false;
    }





    template <typename _ArrayType>
    bool array<_ArrayType>::__common_iterator::operator>=(const array<_ArrayType>::__common_iterator &_it) const {
        return (this->current >= _it.current) ? true : false;
    }





    template <typename _ArrayType>
    bool array<_ArrayType>::__common_iterator::operator<(const array<_ArrayType>::__common_iterator &_it) const {
        return (this->current < _it.current) ? true : false;
    }





    template <typename _ArrayType>
    bool array<_ArrayType>::__common_iterator::operator<=(const array<_ArrayType>::__common_iterator &_it) const {
        return (this->current <= _it.current) ? true : false;
    }





    template <typename _ArrayType>
    typename array<_ArrayType>::__common_iterator &array<_ArrayType>::__common_iterator::operator++() {
        ++ this->current;

        return *this;
    }






    template <typename _ArrayType>
    typename array<_ArrayType>::__common_iterator &array<_ArrayType>::__common_iterator::operator--() {
        -- this->current;

        return *this;
    }






    template <typename _ArrayType>
    typename array<_ArrayType>::__common_iterator &array<_ArrayType>::__common_iterator::operator++(int) {
        this->current ++;

        return *this;
    }






    template <typename _ArrayType>
    typename array<_ArrayType>::__common_iterator &array<_ArrayType>::__common_iterator::operator--(int) {
        this->current --;

        return *this;
    }




    template<typename _ArrayType>
    array<_ArrayType>::const_iterator::const_iterator() {}





    template<typename _ArrayType>
    array<_ArrayType>::const_iterator::const_iterator(_ArrayType *elem) {
        this->current = elem;
    }





    template<typename _ArrayType>
    const _ArrayType &array<_ArrayType>::const_iterator::operator*() const {
        return *this->current;
    }





    template<typename _ArrayType>
    const typename array<_ArrayType>::const_iterator array<_ArrayType>::const_iterator::operator+(int value) const {
        array<_ArrayType>::const_iterator temp = this->current + value;

        return temp;
    }





    template<typename _ArrayType>
    const typename array<_ArrayType>::const_iterator array<_ArrayType>::const_iterator::operator-(int value) const {
        array<_ArrayType>::const_iterator temp = this->current - value;

        return temp;
    }




    template<typename _ArrayType>
    array<_ArrayType>::iterator::iterator() {}




    template<typename _ArrayType>
    array<_ArrayType>::iterator::iterator(_ArrayType *elem) {
        this->current = elem;
    }




    template<typename _ArrayType>
    _ArrayType& array<_ArrayType>::iterator::operator*() {
        return *this->current;
    }




    template<typename _ArrayType>
    typename array<_ArrayType>::iterator& array<_ArrayType>::iterator::operator+=(int value) {
        this->current += value;

        return *this;
    }




    template<typename _ArrayType>
    typename array<_ArrayType>::iterator& array<_ArrayType>::iterator::operator-=(int value) {
        this->current -= value;

        return *this;
    }




    template<typename _ArrayType>
    typename array<_ArrayType>::iterator array<_ArrayType>::iterator::operator+(int value) {
        array<_ArrayType>::iterator temp;

        return this->current + value;
    }




    template<typename _ArrayType>
    typename array<_ArrayType>::iterator array<_ArrayType>::iterator::operator-(int value) {
        array<_ArrayType>::iterator temp;

        return this->current - value;
    }





    template <typename _ArrayType>
    std::ostream &operator<<(std::ostream &left, const array<_ArrayType> &ob) {
        left << "[";
        for (int i=0; i<ob.length(); i++) {
            if (ob.length() - 1 == i) {
                left << ob[i];   
            }
            else {
                left << ob[i] << ", "; 
            }
        }
        left << "]";

        return left; 
    }






    template <typename _ArrayType>
    std::istream &operator>>(std::istream &left, const array<_ArrayType> &ob) {
        _ArrayType user_input;
        std::cout << "Enter value at " << ob.length() << " index position: ";
        left >> user_input;

        ob.push_back(user_input);    

        return left;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::selection_sort(const bool rev) {
        if (!rev) {
            for (int i=0; i<this->length(); i++) {
                int j = i;
                _ArrayType min = this->arr[j];

                for (int k=i+1; k<this->length(); k++) {
                    if (this->arr[k] < min) {
                        j = k;
                        min = this->arr[j];
                    }
                }

                _ArrayType temp = this->arr[i];
                this->arr[i]= this->arr[j];
                this->arr[j] = temp;
            }
        }
        else {
            for (int i=0; i<this->length(); i++) {
                int j = i;
                _ArrayType max = this->arr[j];

                for (int k=i+1; k<this->length(); k++) {
                    if (this->arr[k] > max) {
                        j = k;
                        max = this->arr[j];
                    }
                }

                _ArrayType temp = this->arr[i];
                this->arr[i]= this->arr[j];
                this->arr[j] = temp;
            }
        }

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::bubble_sort(const bool rev) {
        if (!rev) {
            for (int i=this->length(); i>0; i--) {
                for (int j=this->length()-1; j>0; j--) {

                    if (this->arr[j] < this->arr[j-1]) {
                        _ArrayType temp = this->arr[j];
                        this->arr[j] = this->arr[j-1];
                        this->arr[j-1] = temp;
                    }
                }
            }
        }
        else {
            for (int i=this->length(); i>0; i--) {
                for (int j=this->length()-1; j>0; j--) {

                    if (this->arr[j] > this->arr[j-1]) {
                        _ArrayType temp = this->arr[j];
                        this->arr[j] = this->arr[j-1];
                        this->arr[j-1] = temp;
                    }
                }
            }
        }

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::insertion_sort(const bool rev) {
        if (!rev) {
            int j;
            _ArrayType key;
            for (int i=1; i<this->length(); i++) {
                key = this->arr[i];
                j = i - 1;
                while ((key < this->arr[j]) && (j >= 0)) {
                    this->arr[j+1] = this->arr[j];
                    j --;
                }
                this->arr[j+1] = key;
            }
        }
        else {
            int j;
            _ArrayType key;
            for (int i=1; i<this->length(); i++) {
                key = this->arr[i];
                j = i - 1;
                while ((key > this->arr[j]) && (j >= 0)) {
                    this->arr[j+1] = this->arr[j];
                    j --;
                }
                this->arr[j+1] = key;
            }
        }

        return *this;
    }





    template <typename _ArrayType>
    array<_ArrayType> array<_ArrayType>::improved_selection_sort(const bool rev) {
        if (!rev) {
            _ArrayType temp;
            int max_i;
            int start = 0;

            while (start < this->length()) {
                max_i = start;
                for (int i=start; i<this->length(); i++) {
                    if (this->arr[i] < this->arr[max_i]) {
                        max_i = i;
                    }
                }
                temp = this->arr[max_i];
                this->arr[max_i] = this->arr[start];
                this->arr[start] = temp;

                start ++;
            }
        }
        else {
            _ArrayType temp;
            int max_i;
            int start = 0;

            while (start < this->length()) {
                max_i = start;
                for (int i=start; i<this->length(); i++) {
                    if (this->arr[i] > this->arr[max_i]) {
                        max_i = i;
                    }
                }
                temp = this->arr[max_i];
                this->arr[max_i] = this->arr[start];
                this->arr[start] = temp;

                start ++;
            }
        }

        return *this;
    }





    template <typename _ArrayType>
    bool array<_ArrayType>::__link_iter_to_arr(array<_ArrayType>::iterator &it) {
        for (typename array<_ArrayType>::iterator arr_it=this->begin(); arr_it!=this->end(); arr_it++) {
            if (arr_it == it) {
                return true;
            }
        }
        return false;
    }





    template <typename _ArrayType>
    bool array<_ArrayType>::__link_iter_to_arr(array<_ArrayType>::const_iterator &it) {
        for (typename array<_ArrayType>::iterator arr_it=this->begin(); arr_it!=this->end(); arr_it++) {
            if (arr_it == it) {
                return true;
            }
        }
        return false;
    }





    template <typename _ArrayType>
    bool array<_ArrayType>::__link_iter_to_vector(std::vector<_ArrayType> &vect, typename std::vector<_ArrayType>::iterator &it) const {
        for (typename std::vector<_ArrayType>::iterator vect_it=vect.begin(); vect_it!=vect.end(); vect_it++) {
            if (vect_it == it) {
                return true;
            }
        }
        return false;
    }





    template <typename _ArrayType>
    bool array<_ArrayType>::__link_iter_to_vector(const std::vector<_ArrayType> &vect, typename std::vector<_ArrayType>::const_iterator &it) const {
        for (typename std::vector<_ArrayType>::const_iterator vect_it=vect.begin(); vect_it!=vect.end(); vect_it++) {
            if (vect_it == it) {
                return true;
            }
        }
        return false;
    }




    template <typename _ArrayType>
    int array<_ArrayType>::__get_random_number(const int min, const int max) const {
        static double fraction { 1.0 / (RAND_MAX + 1.0) };
        return min + ((max - min + 1) * (std::rand() * fraction));
    }





    template <typename _ArrayType>
    array<int> array<_ArrayType>::__new_indexes() const {
        array<int> new_indexes;

        std::srand(std::time(nullptr));

        int n;
        bool append;
        while (this->length() > new_indexes.length()) {
            append = true;

            n = this->__get_random_number(0, this->length()-1);
            for (int i=0; i<new_indexes.length(); i++) {
                if (n == new_indexes[i]) {
                    append = false;
                    break;
                }
            }
            if (append) {
                new_indexes.push_back(n);
            }
        }

        return new_indexes;
    }
}

#endif
