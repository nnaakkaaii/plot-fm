import { atom } from 'recoil';

const companyState = atom<string>({
    key: 'companyState',
    default: '',
});

export default companyState;